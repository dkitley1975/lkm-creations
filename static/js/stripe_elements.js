var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();
var style = {
	base: {
		color: "#000",
		fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
		fontSmoothing: "antialiased",
		fontSize: "16px",
		"::placeholder": {
			color: "#aab7c4",
		},
	},
	invalid: {
		color: "#dc3545",
		iconColor: "#dc3545",
	},
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
	var errorDiv = document.getElementById("card-errors");
	if (event.error) {
		var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
		$(errorDiv).html(html);
	} else {
		errorDiv.textContent = "";
	}
});

// Handle form submit
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
	//This prevents the form from submitting immediately
	ev.preventDefault();
	//This disables the submit button after the initial press
	//and  then enables it after a response, to prevent multiple submits
	card.update({ disabled: true });
	$("#submit-button").attr("disabled", true);
	$("#payment-form").fadeToggle(100);
	//This shows the overlay Spinner whilst waiting for Stripe
	$("#loading-overlay").fadeToggle(100);

	// Grabs data which can not be sent within the Stripe intent and
	// sends it to the cache_checkout_data view

	// gets a boolean response from the form regarding if the Save address details checkbox is checked
	var saveInfo = Boolean($("#id-save-info").attr("checked"));
	//Grabs the  {% csrf_token %} from within the form
	var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
	//Grabs the stripe token from the card element
	//along with the CSRF token and the Save info
	//and wraps it in a JSON object
	var postData = {
		csrfmiddlewaretoken: csrfToken,
		save_info: saveInfo,
		client_secret: clientSecret,
	};
	// The url/View for the POST request
	var url = "/checkout/cache_checkout_data/";

	$.post(url, postData)
		.done(function () {
			// the cache_checkout_data updates the payment intent and
			// returns a 200 response,
			// the confirm payment is then called from  stripe
			stripe
				.confirmCardPayment(clientSecret, {
					payment_method: {
						card: card,
						billing_details: {
							name: $.trim(form.full_name.value),
							phone: $.trim(form.phone_number.value),
							email: $.trim(form.email.value),
							address: {
								line1: $.trim(form.street_address1.value),
								line2: $.trim(form.street_address2.value),
								city: $.trim(form.town_or_city.value),
								country: $.trim(form.country.value),
								state: $.trim(form.county.value),
							},
						},
					},
					shipping: {
						name: $.trim(form.full_name.value),
						phone: $.trim(form.phone_number.value),
						address: {
							line1: $.trim(form.street_address1.value),
							line2: $.trim(form.street_address2.value),
							city: $.trim(form.town_or_city.value),
							country: $.trim(form.country.value),
							postal_code: $.trim(form.postcode.value),
							state: $.trim(form.county.value),
						},
					},
				})
				.then(function (result) {
					//If there is an error
					if (result.error) {
						// Show error  information to client (e.g., incorrect details)
						var errorDiv = document.getElementById("card-errors");
						var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
						$(errorDiv).html(html);
						// re-enable the submit button and form
						//hides the spinning overlay
						$("#payment-form").fadeToggle(100);
						$("#loading-overlay").fadeToggle(100);
						card.update({ disabled: false });
						$("#submit-button").attr("disabled", false);
					} else {
						// With any luck the payment has been processed!
						// a succeeded message is sent to the server and the form submitted
						if (result.paymentIntent.status === "succeeded") {
							form.submit();
						}
					}
				});
		})
		.fail(function () {
			// Reloads the page, to show the error in django messages.
			// TODO Need to find if there is a way to display
			// the messages without forcing reloads.
			location.reload();
		});
});

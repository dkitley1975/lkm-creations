/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here:
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elem = document.getElementById("submit-button");

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
	ev.preventDefault();
	card.update({ disabled: true });
	$("#submit-button").attr("disabled", true);
	var receipientName = document.getElementById("id_full_name").value;
	var receipientEmail = document.getElementById("div_id_email").value;
	var receipientPhone = document.getElementById("div_id_phone_number").value;
	var receipientStreetAddress1 = document.getElementById(
		"div_id_street_address1"
	).value;
	var receipientStreetAddress1 = document.getElementById(
		"div_id_street_address2"
	).value;
	var receipientCity = document.getElementById("div_id_town_or_city").value;
	var receipientCounty = document.getElementById("div_id_county").value;
	var receipientPostalCode = document.getElementById("div_id_postcode").value;
	var receipientCountry = document.getElementById("div_id_country").value;

	stripe
		.confirmCardPayment(clientSecret, {
			payment_method: {
				card: card,
				delivery_details: {
					address: {
						line1: receipientStreetAddress1,
						line2: receipientStreetAddress2,
						city: receipientCity,
						state: receipientCounty,
						postal_code: receipientPostalCode,
						country: receipientCountry,
					},
					email: receipientEmail,
					name: receipientName,
					phone: receipientPhone,
				},
			},
		})
		.then(function (result) {
			if (result.error) {
				var errorDiv = document.getElementById("card-errors");
				var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
				$(errorDiv).html(html);
				card.update({ disabled: false });
				$("#submit-button").attr("disabled", false);
			} else {
				if (result.paymentIntent.status === "succeeded") {
					form.submit();
				}
			}
		});
});

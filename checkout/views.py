import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)

from basket.custom_context_processors import basket_contents
from checkout.forms import OrderForm
from checkout.models import OrderDetails, OrderLineItem
from products.models import Product


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_currency = settings.STRIPE_CURRENCY
    if request.method == "POST":
        basket = request.session.get("basket", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your basket "
                            "wasn't found in our database. "
                            "Please call us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("checkout:checkout"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse(
                    "checkout:checkout-success", args=[order.order_number]
                )
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )
    else:
        basket = request.session.get("basket", {})
        if not basket:
            messages.error(
                request, "There's nothing in your basket at the moment"
            )
            return redirect(reverse("store:products"))

        current_bag = basket_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=stripe_currency,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. \
            Did you forget to set it in your environment?",
        )

    template = "checkout/pages/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    request.session.get("save_info")
    order = get_object_or_404(OrderDetails, order_number=order_number)
    messages.success(
        request,
        f"Your order was successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "basket" in request.session:
        del request.session["basket"]

    template = "checkout/pages/checkout-success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)


def adjust_basket(request, item_id):
    """
    Adjust the basket based on the quantity of the product.
    If the quantity is greater than 0,
    add the product to the basket.
    If the quantity is 0, remove the product from the basket.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})
    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request,
            (
                f"You have updated the product {product.name} "
                f"quantity to {basket[item_id]}"
            ),
        )
    else:
        basket.pop[item_id]
        messages.success(
            request,
            (
                f"You have removed the product {product.name}\
                    from your basket."
            ),
        )
    request.session["basket"] = basket
    return redirect(reverse("summary"))


def remove_from_basket(request, item_id):
    """
    Remove an item from the basket.
    """
    try:
        basket = request.session.get("basket", {})
        basket.pop(item_id)
        request.session["basket"] = basket
        product = get_object_or_404(Product, pk=item_id)
        messages.success(
            request,
            (
                f"You have removed the product {product.name} \
                    from your basket."
            ),
        )
        return HttpResponse(status=200)

    except Exception as e:
        """
        Handle the error if there is an error removing an item.
        @param e - the error message
        """
        messages.error(
            request,
            f"There was an error removing item: {e}, please try again.",
        )
        return HttpResponse(status=500)

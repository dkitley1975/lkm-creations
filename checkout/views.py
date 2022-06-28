import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)
from django.views.decorators.http import require_POST

from basket.custom_context_processors import basket_contents
from checkout.forms import OrderForm
from checkout.models import OrderDetails, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


@require_POST
def cache_checkout_data(request):
    """
    Cache the checkout data in the session.
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "basket": json.dumps(request.session.get("basket", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            (
                "Sorry there was a problem \
            processing your payment.\
            Please try again later."
            ),
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Render the checkout page.
    """
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
            """
            If the form is valid, save the order and
            the order line items.
            """
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
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
                            "One of the products in your basket \
                            wasn't found in our database. \
                            Please call us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("checkout"))
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout-success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please check your information.",
            )
    else:
        basket = request.session.get("basket", {})
        if not basket:
            messages.error(
                request, "There's nothing in your basket at the moment"
            )
            return redirect(reverse("products"))
        current_bag = basket_contents(request)
        total = current_bag["grand_total"]
        # stripe needs the price in pence
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        """ Create a payment intent for Stripe. """
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=stripe_currency,
        )
        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            """
            If the user is authenticated, grab their profile and
            fill in their details in the order form.
            Otherwise, just create an empty order form.
            """
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                        "town_or_city": profile.default_town_or_city,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "county": profile.default_county,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(
            request,
            (
                "Stripe public key is missing. \
            Did you forget to set it in your environment?"
            ),
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
    Save the order details and
    the user profile details if the user is logged in.
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(OrderDetails, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(
                profile_data, instance=profile
            )
            if user_profile_form.is_valid():
                user_profile_form.save()
    messages.success(
        request,
        (
            f"Congratulations your order was successfully processed! \
        Your order reference is {order_number}. A confirmation \
        email will be sent to {order.email}."
        ),
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
        """
        messages.error(
            request,
            (f"There was an error removing item: {e}, please try again.",),
        )
        return HttpResponse(status=500)

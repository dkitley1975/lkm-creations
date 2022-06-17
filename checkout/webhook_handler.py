# Code based on the Code Institute BoutiqueAdo walkthrough
# Altered to fit my needs
import json
import time

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from products.models import Product

from .models import OrderDetails, OrderLineItem

# from profiles.models import UserProfile


class StripeWH_Handler:
    def __init__(self, request):
        """
        assign the request as a attribute of the class
        """
        self.request = request

    # def _send_confirmation_email(self, order):
    #     """Send the user a confirmation email"""
    #     cust_email = order.email
    #     subject = render_to_string(
    #         "checkout/confirmation_emails/confirmation_email_subject.txt",
    #         {"order": order},
    #     )
    #     body = render_to_string(
    #         "checkout/confirmation_emails/confirmation_email_body.txt",
    #         {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
    #     )

    #     send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle the event that is sent from the webhook.
        This function is called whenever a new event is received.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook.
        """
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        order_grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        # removes empty fields adding  None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = (
                    shipping_details.address.postal_code
                )
                profile.default_town_or_city = (
                    shipping_details.address.city
                )
                profile.default_street_address1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address2 = (
                    shipping_details.address.line2
                )
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = OrderDetails.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=order_grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except OrderDetails.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | SUCCESS: '
                    "Verified order already in database"
                ),
                status=200,
            )
        else:
            order = None
            try:
                order = OrderDetails.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, quantity in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | SUCCESS: '
                "Created order in webhook"
            ),
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a failed payment intent.
        This is a webhook for Stripe.
        The event will be received from Stripe.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )

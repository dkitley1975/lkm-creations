from django.urls import path

from checkout import views

from .webhooks import webhook


urlpatterns = [
    path("", views.checkout, name="checkout"),
    path(
        "checkout-success/<order_number>",
        views.checkout_success,
        name="checkout-success",
    ),
    # stripe
    path(
        "cache_checkout_data/",
        views.cache_checkout_data,
        name="cache_checkout_data",
    ),
    path("wh/", webhook, name="webhook"),
]

from django.urls import path

from checkout import views

app_name = "checkout"

urlpatterns = [
    path("checkout", views.checkout, name="checkout"),
    path(
        "checkout-success/<order_number>",
        views.checkout_success,
        name="checkout-success",
    ),
]

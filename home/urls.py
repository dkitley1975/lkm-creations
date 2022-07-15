from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home"),
    path("contact-us", views.ContactUs.as_view(), name="contact-us"),
    path(
        "documents/privacy-policy",
        TemplateView.as_view(
            template_name="home/pages/privacy-policy.html"
        ),
        name="privacy-policy",
    ),
    path(
        "documents/terms-of-service-policy",
        TemplateView.as_view(
            template_name="home/pages/terms-of-service-policy.html"
        ),
        name="terms-of-service-policy",
    ),
    path(
        "documents/returns-policy",
        TemplateView.as_view(
            template_name="home/pages/returns-policy.html"
        ),
        name="returns-policy",
    ),
    path(
        "documents/disclaimer-policy",
        TemplateView.as_view(
            template_name="home/pages/disclaimer-policy.html"
        ),
        name="disclaimer-policy",
    ),
    path(
        "documents/shipping-policy",
        TemplateView.as_view(
            template_name="home/pages/shipping-policy.html"
        ),
        name="shipping-policy",
    ),
    path(
        "documents/cookie-policy",
        TemplateView.as_view(
            template_name="home/pages/cookie-policy.html"
        ),
        name="cookie-policy",
    ),
]

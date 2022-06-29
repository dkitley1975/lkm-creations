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
    ),
    path(
        "documents/terms-of-service-policy",
        TemplateView.as_view(
            template_name="home/pages/terms-of-service-policy.html"
        ),
    ),
    path(
        "documents/returns-policy",
        TemplateView.as_view(
            template_name="home/pages/returns-policy.html"
        ),
    ),
    path(
        "documents/disclaimer-policy",
        TemplateView.as_view(
            template_name="home/pages/disclaimer-policy.html"
        ),
    ),
    path(
        "documents/shipping-policy",
        TemplateView.as_view(
            template_name="home/pages/shipping-policy.html"
        ),
    ),
    path(
        "documents/cookie-policy",
        TemplateView.as_view(
            template_name="home/pages/cookie-policy.html"
        ),
    ),
]

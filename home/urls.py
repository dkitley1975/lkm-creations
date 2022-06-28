from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home"),
    path("contact-us", views.ContactUs.as_view(), name="contact-us"),
]

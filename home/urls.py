from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home"),
    path('contact-us', views.ContactUs.as_view(), name='contact-us'),
]

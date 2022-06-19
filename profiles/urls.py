from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        "order-summary/<order_number>/",
        views.order_summary,
        name="order-summary",
    ),
]

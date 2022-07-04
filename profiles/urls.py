from django.urls import path

from . import views
from .views import profileUpdate

urlpatterns = [
    path("", views.DashboardView, name="dashboard"),
    path("order-history", views.OrderHistoryView, name="order-history"),
    path(
        "order-summary/<order_number>/",
        views.order_summary,
        name="order-summary",
    ),
    path(
        "profile-update",
        profileUpdate,
        name="profile-update",
    ),
    path("connections", views.ConnectionsView, name="connections"),
]

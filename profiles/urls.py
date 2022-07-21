from django.urls import path

from . import views

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
        views.profileUpdate,
        name="profile-update",
    ),
    path(
        "delete-account",
        views.deleteAccountView,
        name="delete-account",
    ),
    path("connections", views.ConnectionsView, name="connections"),
    path("remove_account", views.remove_account, name="remove_account"),
]

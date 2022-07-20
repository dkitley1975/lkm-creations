from django.urls import path

from store import views

urlpatterns = [
    path("products", views.store_front, name="products"),
    path("sale", views.products_on_sale, name="sale"),
    path("<slug:slug>/", views.product_detail, name="product-detail"),
    path(
        "category/<slug:category_slug>/",
        views.category_list,
        name="category-list",
    ),
    path(
        "review-delete/<int:id>/",
        views.review_delete,
        name="review-delete",
    ),
]

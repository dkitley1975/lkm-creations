from django.shortcuts import render

from products.models import Product


def index(request):
    """
    A view to return the index page
    Showing the 6 most recently created items.
    filtering out non sale items,
    items with a sale price of 0.00
    and items that are not in stock.
    """

    products = Product.available_items.all().order_by("-created_at")[0:6]

    return render(request, "home/index.html", {"products": products})

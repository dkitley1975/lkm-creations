from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from .forms import CreateNewProductForm
from .models import Product


# Create your views here.
class ProductCreate(CreateView):
    """
    Create a new product page.
    """

    model = Product
    template_name = "product/pages/product-creation.html"
    form_class = CreateNewProductForm
    success_url = reverse_lazy("products")


class ProductUpdate(UpdateView):
    """
    Update the product page.
    """

    model = Product
    template_name = "product/pages/product-update.html"
    form_class = CreateNewProductForm
    success_url = reverse_lazy("products")


class ProductDelete(DeleteView):
    """
    Delete a product from the database.
    """

    model = Product
    template_name = "product/pages/product-delete.html"
    success_url = reverse_lazy("products")

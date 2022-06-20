from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from products.models import Product
from django.contrib import messages
from django.urls import reverse_lazy


from .forms import ContactForm


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



class ContactUs(FormView):
    template_name = "home/pages/contact-us.html"
    form_class = ContactForm
    success_url ="contact-us"

    def form_valid(self, form):
        """
        Override the form_valid method to send the form to the server.
        """
        # Calls the custom send method
        form.send()
        # This will add the flash message after email being valid
        messages.success(self.request, "Thank you for contacting us..\
                Your message has been sent, \
                and you should receive a copy in your inbox soon.")
        return super().form_valid(form)

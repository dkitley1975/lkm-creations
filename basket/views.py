from django.contrib import messages
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)

from products.models import Product


# Create your views here.
def summary(request):
    """
    This function is used to create a summary of the basket.
    It is called when the user clicks on the basket.
    """
    return render(request, "basket/pages/summary.html")


def add_to_basket(request, item_id):
    """
    Add an item to the basket.
    If the item is already in the basket,
    add the quantity. Otherwise,
    add the item to the basket.
    @param request - the request object
    @param item_id - the id of the item to add to the basket
    @returns the redirect url
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get("basket", {})
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request,
            (
                f"You have updated the product {product.name} "
                f"quantity to {basket[item_id]}"
            ),
        )
    else:
        basket[item_id] = quantity
        messages.success(
            request,
            (
                f"You have added {basket[item_id]} of the product {product.name} "
                "to your basket"
            ),
        )
    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the basket based on the quantity of the product.
    If the quantity is greater than 0,
    add the product to the basket.
    If the quantity is 0, remove the product from the basket.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})
    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request,
            (
                f"You have updated the product {product.name} "
                f"quantity to {basket[item_id]}"
            ),
        )
    else:
        basket.pop[item_id]
        messages.success(
            request,
            (
                f"You have removed the product {product.name}\
                    from your basket."
            ),
        )
    request.session["basket"] = basket
    return redirect(reverse("summary"))


def remove_from_basket(request, item_id):
    """
    Remove an item from the basket.
    """
    try:
        basket = request.session.get("basket", {})
        basket.pop(item_id)
        request.session["basket"] = basket
        product = get_object_or_404(Product, pk=item_id)
        messages.success(
            request,
            (
                f"You have removed the product {product.name} \
                    from your basket."
            ),
        )
        return HttpResponse(status=200)

    except Exception as e:
        """
        Handle the error if there is an error removing an item.
        @param e - the error message
        """
        messages.error(
            request,
            f"There was an error removing item: {e}, please try again.",
        )
        return HttpResponse(status=500)

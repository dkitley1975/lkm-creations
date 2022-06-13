from django.shortcuts import HttpResponse, redirect, render, reverse


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
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get("basket", {})
    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):

    quantity = int(request.POST.get("quantity"))
    basket = request.session.get("basket", {})
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop[item_id]
    request.session["basket"] = basket
    return redirect(reverse("summary"))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        basket = request.session.get("basket", {})
        basket.pop(item_id)
        request.session["basket"] = basket
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)

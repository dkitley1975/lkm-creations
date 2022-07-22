from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from products.models import Category, Product, Review


# Create your views here.
def category_list(request, category_slug=None):
    """
    Given a request and a category slug, return the category page.
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.available_items.filter(category=category)
    return render(
        request,
        "store/pages/category.html",
        {"category": category, "products": products},
    )


def store_front(request):
    """
    View function for all products
    """
    products = Product.available_items.all()
    query = None
    sort = None
    sort_direction = None
    if request.GET:
        if "sort" in request.GET:
            # Sort the products based on the sortkey and sort direction.
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "sort_direction" in request.GET:
                sort_direction = request.GET["sort_direction"]
                if sort_direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)
        if "q" in request.GET:
            # If the user has entered a search query,
            # filter the products accordingly.
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)
    current_sorting = f"{sort}_{sort_direction}"
    context = {
        "products": products,
        "search_term": query,
        "current_sorting": current_sorting,
    }
    return render(request, "store/pages/products.html", context)


def product_detail(request, slug):
    """
    Render the product detail page.
    """
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(
                request, "You must be logged to leave a review."
            )
            return redirect(reverse("login"))
        rating = request.POST.get("rating", 5)
        content = request.POST.get("content", "")
        if content:
            reviews = Review.objects.filter(
                created_by=request.user, product=product
            )
            if reviews.exists():
                messages.error(
                    request,
                    "You have already left a review for this product.",
                )
                return redirect("product-detail", slug=slug)
            else:
                Review.objects.create(
                    created_by=request.user,
                    product=product,
                    rating=rating,
                    content=content,
                )
                messages.success(
                    request, "Your review has been submitted."
                )
                return redirect("product-detail", slug=slug)

        messages.success(
            request, "You have successfully submitted your review."
        )
        return redirect("product-detail", slug=slug)
    lastreview = Review.objects.filter(product=product).last()
    context = {
        "product": product,
        "lastreview": lastreview,
    }

    return render(request, "store/pages/product-detail.html", context)


@login_required(login_url="/login/")
def review_delete(request, id):
    """
    Delete a reviews
    """
    current_user = request.user
    Review.objects.filter(id=id, created_by=current_user).delete()
    messages.success(request, "Your review has been deleted.")
    next = request.GET.get("next", "products")
    return HttpResponseRedirect(next)


def products_on_sale(request):
    """
    Render the product sale.
    filtering out non sale items,
    items with a sale price of 0.00
    and items that are not in stock.
    """
    products = (
        Product.available_items.exclude(sale_price__isnull=True)
        .exclude(sale_price__exact="0.00")
        .order_by("-sale_price")
    )
    return render(
        request, "store/pages/sale-products.html", {"products": products}
    )

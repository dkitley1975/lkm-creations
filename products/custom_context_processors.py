from django.db.models import Count

from .models import Category

# Create your views here.


def categories(request):
    """
    View function for all categories.
    Counts all the items with the related name
    'product' in each category.
    returns a list of categories with a product
    count over 0
    """

    return {
        "categories": Category.objects.annotate(
            product_count=Count("product")
        )
        .filter(product_count__gt=0)
        .order_by("product_count")
    }

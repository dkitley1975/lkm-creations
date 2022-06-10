import admin_thumbnails
from django.contrib import admin

from .models import Category, Colour, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    The admin interface for the Category model.
    """

    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["name"]


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    """
    The admin interface for the Colour model.
    """

    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["name"]


@admin.register(Product)
@admin_thumbnails.thumbnail("image", "Thumbnail")
class ProductAdmin(admin.ModelAdmin):
    """
    The admin interface for the Product model.
    """

    save_on_top = True
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "keywords",
                )
            },
        ),
        (
            "Imagery",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "image_thumbnail",
                    "image",
                    "image_alt_text",
                ),
            },
        ),
        (
            "Price and costs",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "unit_cost_price",
                    "retail_price",
                    "sale_price",
                ),
            },
        ),
        (
            None,
            {
                "fields": (
                    "sku",
                    ("category", "colour"),
                    ("weight", "size"),
                    ("is_washable", "in_stock", "is_active"),
                    "slug",
                )
            },
        ),
    )

    list_display = [
        "name",
        "retail_price",
        "sale_price",
        "in_stock",
        "is_active",
        "image_thumbnail",
    ]
    list_filter = ["name", "in_stock", "is_active"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["retail_price", "sale_price", "in_stock", "is_active"]

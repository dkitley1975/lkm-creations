import admin_thumbnails
from django.contrib import admin

from .models import SiteInfo


@admin.register(SiteInfo)
@admin_thumbnails.thumbnail("image", "Thumbnail")
class SiteInfoAdmin(admin.ModelAdmin):
    """
    This is a custom admin class for the model.
    """

    save_on_top = True
    save_on_top = True
    fieldsets = (
        (
            "Site Contact Information",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": ["email_address", "phone_number"],
            },
        ),
        (
            "Site Social Links Information",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": [
                    "github_url",
                    "linkedin_url",
                    "facebook_url",
                    "twitter_url",
                ],
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
            "Delivery Price and costs",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": [
                    "free_delivery_over",
                    "delivery_cost_price",
                    "delivery_price",
                ],
            },
        ),
        (
            "Universal Site Message",
            {
                "classes": ("show", "extrapretty"),
                "fields": ["alert_message"],
            },
        ),
        (None, {"fields": ["is_active"]}),
    )

    list_display = [
        "image_thumbnail",
        "alert_message",
        "email_address",
        "phone_number",
        "delivery_cost_price",
        "delivery_price",
        "is_active",
    ]

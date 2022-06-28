from django.contrib import admin

from .models import OrderDetails, OrderLineItem, OrderStatus


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    """
    The admin interface for the Category model.
    """

    list_display = [
        "order_status",
    ]
    ordering = ["order_status"]


class OrderLineItemAdminInLine(admin.TabularInline):
    verbose_name = "Order Item"
    verbose_name_plural = "Order Items"
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderDetailsAdmin(admin.ModelAdmin):
    verbose_name = "Orders"
    verbose_name_plural = "Orders"
    inlines = (OrderLineItemAdminInLine,)
    readonly_fields = (
        "order_number",
        # "user_profile",
        "order_date",
        "delivery_charge",
        "order_subtotal",
        "grand_total",
        "original_basket",
        "stripe_pid",
    )
    fieldsets = (
        (
            "Details",
            {
                "classes": ("extrapretty"),
                "fields": (
                    ("order_number", "order_date"),
                    "order_status",
                    "delivery_charge",
                    "order_subtotal",
                    "grand_total",
                    "original_basket",
                    "stripe_pid",
                ),
            },
        ),
        (
            "Contact Details",
            {
                "classes": (
                    "collapse",
                    "extrapretty",
                ),
                "fields": (
                    "user_profile",
                    "full_name",
                    "phone_number",
                    "email",
                ),
            },
        ),
        (
            "Delivery Address",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "street_address1",
                    "street_address2",
                    "town_or_city",
                    "county",
                    "country",
                    "postcode",
                ),
            },
        ),
    )
    list_display = (
        "order_number",
        "order_status",
        "order_date",
        "full_name",
        "grand_total",
    )
    ordering = ("-order_date",)


admin.site.register(OrderDetails, OrderDetailsAdmin)

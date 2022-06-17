import uuid

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from products.models import Product
from siteadmin.custom_context_processors import site_info
from profiles.models import UserProfile

# Create your models here.
class OrderDetails(models.Model):

    # user contact details
    user_profile = (
        models.ForeignKey(
            UserProfile,
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="orders",
        ),
    )
    phone_number = models.CharField(
        max_length=20,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Contact Number"),
    )
    full_name = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Full Name"),
    )
    email = models.EmailField(
        max_length=254,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Email Address"),
    )
    # Order Details
    order_number = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        verbose_name=("Order Number"),
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        verbose_name=("Order Date"),
    )

    # user address details
    street_address1 = models.CharField(
        max_length=80,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Address Line 1"),
    )
    street_address2 = models.CharField(
        max_length=80,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("Address Line 2"),
    )
    town_or_city = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Town or City"),
    )
    county = models.CharField(
        max_length=50,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("County"),
    )
    country = CountryField(
        unique=False,
        blank=False,
        null=False,
        blank_label="Country *",
    )
    postcode = models.CharField(
        max_length=10,
        unique=False,
        blank=True,
        null=True,
        verbose_name=("Postcode"),
    )
    # Order values
    delivery_charge = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        unique=False,
        blank=False,
        null=False,
        default=0,
    )
    order_subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    order_grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_basket = models.TextField(blank=False, null=False, default="")
    stripe_pid = models.CharField(
        max_length=254, blank=False, null=False, default=""
    )

    class Meta:
        ordering = ["-order_number"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def _generate_order_number(self):
        """
        Generate a random order number for the current session.
        """
        return uuid.uuid4().hex[:12].upper()

    def update_total(self):
        """
        Update the total of the order.
        This is called after the lineitems are added.
        """
        self.order_subtotal = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )
        if self.order_subtotal < free_delivery_threshold:
            self.delivery_charge = default_delivery_price
        else:
            self.delivery_charge = 0
        self.order_grand_total = self.order_subtotal + self.delivery_charge
        self.save()

    def save(self, *args, **kwargs):
        """
        Saves the order number for the order.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    This is the model for the OrderLineItem.
    It is used to create a line item for each product in the order.
    """

    order = models.ForeignKey(
        OrderDetails,
        related_name="lineitems",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=0)

    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
    )

    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        """
        Save the line item to the database.
        """
        if (
            self.product.sale_price is not None
            and self.product.sale_price > 0
        ):
            unit_price = self.product.sale_price
        else:
            unit_price = self.product.retail_price
        self.unit_price = unit_price
        self.lineitem_total = unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order\
            {self.order.order_number}, item total \
                £{ self.lineitem_total }".format(
            self=self
        )

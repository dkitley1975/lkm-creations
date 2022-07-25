# Generated by Django 3.2.13 on 2022-07-25 01:31

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=20, verbose_name="Contact Number"
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        max_length=50, verbose_name="Full Name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Email Address"
                    ),
                ),
                (
                    "order_number",
                    models.CharField(
                        editable=False,
                        max_length=32,
                        unique=True,
                        verbose_name="Order Number",
                    ),
                ),
                (
                    "order_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Order Date"
                    ),
                ),
                (
                    "street_address1",
                    models.CharField(
                        max_length=80, verbose_name="Address Line 1"
                    ),
                ),
                (
                    "street_address2",
                    models.CharField(
                        blank=True,
                        max_length=80,
                        null=True,
                        verbose_name="Address Line 2",
                    ),
                ),
                (
                    "town_or_city",
                    models.CharField(
                        max_length=50, verbose_name="Town or City"
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="County",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(max_length=2),
                ),
                (
                    "postcode",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Postcode",
                    ),
                ),
                (
                    "delivery_charge",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=6
                    ),
                ),
                (
                    "order_subtotal",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10
                    ),
                ),
                (
                    "grand_total",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("original_basket", models.TextField(default="")),
                (
                    "stripe_pid",
                    models.CharField(default="", max_length=254),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
                "ordering": ["-order_number"],
            },
        ),
        migrations.CreateModel(
            name="OrderStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_status",
                    models.CharField(
                        max_length=20, verbose_name="Order Status"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Order Statuses",
            },
        ),
        migrations.CreateModel(
            name="OrderLineItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "unit_price",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=6
                    ),
                ),
                (
                    "lineitem_total",
                    models.DecimalField(
                        decimal_places=2, editable=False, max_digits=6
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lineitems",
                        to="checkout.orderdetails",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="order_status",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_number",
                to="checkout.orderstatus",
            ),
        ),
        migrations.AddField(
            model_name="orderdetails",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="profiles.userprofile",
            ),
        ),
    ]

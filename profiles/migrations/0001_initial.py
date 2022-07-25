# Generated by Django 3.2.13 on 2022-07-25 13:53

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                    "default_street_address1",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 80",
                        max_length=80,
                        null=True,
                        verbose_name="User Address Line 1",
                    ),
                ),
                (
                    "default_street_address2",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 80",
                        max_length=80,
                        null=True,
                        verbose_name="User Address Line 2",
                    ),
                ),
                (
                    "default_town_or_city",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 50",
                        max_length=50,
                        null=True,
                        verbose_name="User Town or City",
                    ),
                ),
                (
                    "default_county",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 50",
                        max_length=50,
                        null=True,
                        verbose_name="User County",
                    ),
                ),
                (
                    "default_country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                (
                    "default_postcode",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 10",
                        max_length=10,
                        null=True,
                        verbose_name="User Postcode",
                    ),
                ),
                (
                    "default_phone_number",
                    models.CharField(
                        blank=True,
                        help_text="format: max_length: 20",
                        max_length=20,
                        null=True,
                        verbose_name="User Main Contact Number",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

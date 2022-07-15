# Generated by Django 3.2 on 2022-07-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteInfo",
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
                    "alert_message",
                    models.TextField(
                        blank=True,
                        help_text="format: required, max_length: 200",
                        null=True,
                        verbose_name="Site Alert Message",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default/default_image.webp",
                        help_text="format: required, 440px by 320px",
                        upload_to="images/homepage/",
                        verbose_name="Home Page Image",
                    ),
                ),
                (
                    "image_alt_text",
                    models.CharField(
                        help_text="format: required, max_length: 150",
                        max_length=150,
                        verbose_name="alternative text to show if image doesn't load",
                    ),
                ),
                (
                    "store_description",
                    models.TextField(
                        help_text="format: required, max_length: 160,  include keywords, discounts,                 or offers you're selling",
                        max_length=160,
                        verbose_name="Store Description",
                    ),
                ),
                (
                    "store_keywords",
                    models.TextField(
                        help_text="These are the keywords that your site can be searched with on                Google. Make these single words, relevant to your site,                 often searched",
                        verbose_name="Store Keywords, SEO",
                    ),
                ),
                (
                    "free_delivery_over",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": "Please enter a valid price"
                        },
                        help_text="format: max_digits=5, decimal_places=2",
                        max_digits=5,
                        verbose_name="Free Delivery over subtotal price",
                    ),
                ),
                (
                    "delivery_cost_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": "Please enter a valid price"
                        },
                        help_text="format: max_digits=5, decimal_places=2",
                        max_digits=5,
                        verbose_name="delivery cost price",
                    ),
                ),
                (
                    "delivery_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": "Please enter a valid price"
                        },
                        help_text="format: max_digits=5, decimal_places=2",
                        max_digits=5,
                        verbose_name="delivery price",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        help_text="format: required, max_length: 20",
                        max_length=20,
                        verbose_name="Site Phone Number",
                    ),
                ),
                (
                    "email_address",
                    models.EmailField(
                        help_text="format: required, max_length: 50",
                        max_length=50,
                        verbose_name="Site email address",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="format: true=active, false=inactive",
                        unique=True,
                        verbose_name="Active",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="enter date in format: Y-m-d H:M:S, null-true, blank-true",
                        verbose_name="entry created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="enter date in format: Y-m-d H:M:S, null-true, blank-true",
                        verbose_name="entry last updated",
                    ),
                ),
                (
                    "facebook_url",
                    models.URLField(
                        blank=True,
                        help_text="max_length: 250, sample: https://www.facebook.com/lkm-creations",
                        max_length=250,
                        verbose_name="Facebook account url",
                    ),
                ),
                (
                    "linkedin_url",
                    models.URLField(
                        blank=True,
                        help_text="max_length: 250,                 sample: www.linkedin.com/in/david-kitley-mcnamara",
                        max_length=250,
                        verbose_name="Linkedin account url",
                    ),
                ),
                (
                    "github_url",
                    models.URLField(
                        blank=True,
                        help_text="max_length: 250, sample: https://github.com/dkitley1975",
                        max_length=250,
                        verbose_name="Github account url",
                    ),
                ),
                (
                    "twitter_url",
                    models.URLField(
                        blank=True,
                        help_text="max_length: 250, sample: https://twitter.com/McnamaraKitley",
                        max_length=250,
                        verbose_name="Twitter account url",
                    ),
                ),
            ],
            options={
                "verbose_name": "Site Default Information",
                "verbose_name_plural": "Site Default Information",
                "ordering": ["id"],
            },
        ),
    ]

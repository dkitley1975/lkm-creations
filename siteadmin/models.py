from django.db import models

dec_help = "format: max_digits=5, decimal_places=2"
date_help = "enter date in format: Y-m-d H:M:S, null-true, blank-true"


class SiteInfo(models.Model):
    """
    The siteadmin class is a one place are for.
    editing alert messages, delivery prices, contact details, etc.
    """

    alert_message = models.TextField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=("Site Alert Message"),
        help_text=("format: required, max_length: 200"),
    )
    image = models.ImageField(
        upload_to="images/homepage/",
        unique=False,
        null=False,
        blank=False,
        default="images/default/default_image.webp",
        verbose_name=("Home Page Image"),
        help_text=("format: required, 440px by 320px"),
    )
    image_alt_text = models.CharField(
        max_length=150,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("alternative text to show if image doesn't load"),
        help_text=("format: required, max_length: 150"),
    )
    store_description = models.TextField(
        max_length=160,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Store Description"),
        help_text=(
            "format: required, max_length: 160,  include keywords, discounts, \
                or offers you're selling"
        ),
    )
    store_keywords = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Store Keywords, SEO"),
        help_text=(
            "These are the keywords that your site can be searched with on\
                Google. Make these single words, relevant to your site, \
                often searched"
        ),
    )
    free_delivery_over = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Free Delivery over subtotal price"),
        help_text=dec_help,
        error_messages={"name": ("Please enter a valid price")},
    )
    delivery_cost_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("delivery cost price"),
        help_text=dec_help,
        error_messages={"name": ("Please enter a valid price")},
    )
    delivery_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("delivery price"),
        help_text=dec_help,
        error_messages={"name": ("Please enter a valid price")},
    )

    phone_number = models.CharField(
        max_length=20,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Site Phone Number"),
        help_text=("format: required, max_length: 20"),
    )
    email_address = models.EmailField(
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Site email address"),
        help_text=("format: required, max_length: 50"),
    )

    is_active = models.BooleanField(
        default=True,
        unique=True,
        null=False,
        blank=False,
        verbose_name=("Active"),
        help_text=("format: true=active, false=inactive"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=("entry created"),
        help_text=date_help,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        editable=True,
        verbose_name=("entry last updated"),
        help_text=date_help,
    )
    facebook_url = models.URLField(
        max_length=250,
        unique=False,
        null=False,
        blank=True,
        verbose_name=("Facebook account url"),
        help_text=(
            "max_length: 250, sample: https://www.facebook.com/lkm-creations"
        ),
    )
    linkedin_url = models.URLField(
        max_length=250,
        unique=False,
        null=False,
        blank=True,
        verbose_name=("Linkedin account url"),
        help_text=(
            "max_length: 250, \
                sample: www.linkedin.com/in/david-kitley-mcnamara"
        ),
    )
    github_url = models.URLField(
        max_length=250,
        unique=False,
        null=False,
        blank=True,
        verbose_name=("Github account url"),
        help_text=(
            "max_length: 250, sample: https://github.com/dkitley1975"
        ),
    )
    twitter_url = models.URLField(
        max_length=250,
        unique=False,
        null=False,
        blank=True,
        verbose_name=("Twitter account url"),
        help_text=(
            "max_length: 250, sample: https://twitter.com/McnamaraKitley"
        ),
    )

    class Meta:
        """
        The product item meta.
        Vobose_name is the name of the model in the admin.
        Vobose_name_plural is the name of the model in the admin.
        ordering is the order in which the items are displayed.
        """

        verbose_name = "Site Default Information"
        verbose_name_plural = "Site Default Information"
        ordering = ["id"]

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

date_help = _("enter date in format: Y-m-d H:M:S, null-true, blank-true")
dec_help = _("format: max_digits=5, decimal_places=2")
max200_help = _(
    "format: required, letters, numbers, hyphens, max_length: 200"
)
max150_help = _("format: required, max_length: 150")
# Create your models here.


class AvailableItemsManager(models.Manager):
    """
    A custom manager for the Product model.
    This manager filters out inactive products
    and products that are out of stock
    this manager is added to the products model
    https://www.youtube.com/watch?v=rjUmA_pkGtw&t=365s
    Learn the basics of Django's Model Managers and Querysets.
    """

    def get_queryset(self):
        return (
            super(AvailableItemsManager, self)
            .get_queryset()
            .filter(is_active=True)
            .filter(in_stock=True)
        )


class Category(models.Model):
    """
    Inventory Category table.
    """

    name = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=("category name"),
        help_text=max150_help,
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        unique=True,
        blank=False,
        verbose_name=("category safe URL"),
        help_text=max200_help,
    )
    category_keywords = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=("Category Keywords, SEO"),
        help_text=(
            "These are the keywords that your site can be searched with on Google. Make these single words, relevant to your site, often searched"
        ),
    )

    class Meta:
        """
        The product category meta.
        Vobose_name is the name of the model in the admin.
        Vobose_name_plural is the name of the model in the admin.
        ordering is the order in which the items are displayed.
        """

        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ["name"]

    def __str__(self):
        """
        Returns the name of the stock.
        as the primary identification.
        """
        return self.name


class Colour(models.Model):
    """
    Product Colour table.
    """

    name = models.CharField(
        max_length=150,
        null=False,
        unique=True,
        blank=False,
        verbose_name=("colour name"),
        help_text=max150_help,
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        unique=True,
        blank=False,
        verbose_name=("colour safe URL"),
        help_text=max200_help,
    )

    class Meta:
        """
        The product colour meta.
        Vobose_name is the name of the model in the admin.
        Vobose_name_plural is the name of the model in the admin.
        ordering is the order in which the items are displayed.
        """

        verbose_name = "Product Colour"
        verbose_name_plural = "Product Colours"
        ordering = ["name"]

    def __str__(self):
        """
        Returns the name of the colour.
        as the primary identification.
        """
        return self.name


class Product(models.Model):
    """
    Inventory Product details table.
    """

    sku = models.CharField(
        max_length=8,
        null=False,
        unique=False,
        blank=False,
        verbose_name=("product sku"),
        help_text=("format: required, max_length: 8"),
    )
    name = models.CharField(
        max_length=150,
        null=False,
        unique=True,
        blank=False,
        verbose_name=("product name"),
        help_text=max150_help,
    )

    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    colour = models.ForeignKey(
        Colour, related_name="product", on_delete=models.CASCADE
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product description"),
        help_text=("format: required, max_length: 1000"),
    )
    keywords = models.CharField(
        max_length=150,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product keywords"),
        help_text=(
            "format: required, These are used by Google to search for the product."
            "These are words that are relevant to the product and will be added to the Product Name,"
            "and Category Name. Separate words with a comma:"
            "turtle, bespoke, etc, max_length: 150"
        ),
    )
    is_washable = models.BooleanField(
        default=True,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product is washable"),
        help_text=("format: true=yes, false=no"),
    )
    image = models.ImageField(
        upload_to="images/products/",
        null=True,
        blank=True,
        default="images/default/default_image.png",
    )
    image_alt_text = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("alternative text to show if image doesn't load"),
        help_text=("format: required, max_length: 150"),
    )
    wash_instructions = models.TextField(
        unique=False,
        null=True,
        blank=True,
        default="Machine washable at 30° (hand-wash or delicate mode). \
            Gently squeeze out the remaining water using a towel, \
                do not wring out, stretch or twist to avoid misshape. \
                    Dry flat, do not tumble dry.",
        verbose_name=("Washing Instructions"),
        help_text=("Max_length: 1000"),
    )
    care_instructions = models.TextField(
        unique=False,
        null=True,
        blank=True,
        default="This item may include securely fastened safety eyes. \
            With regular use, these items may require de-pilling.",
        verbose_name=("Additional Care instructions"),
        help_text=("Max_length: 1000"),
    )
    weight = models.FloatField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product weight grams"),
        help_text=("weight in grams"),
    )
    size = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product size description in cm"),
        help_text=("format: product size in CM"),
    )
    unit_cost_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product unit cost price"),
        help_text=dec_help,
        error_messages={"name": ("Please enter a valid price")},
    )
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("store retail price"),
        help_text=dec_help,
        error_messages={"name": ("Please enter a valid price")},
    )
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("sale price"),
        help_text=dec_help,
        error_messages={
            "name": (
                "Please enter a valid price, max_digits=5, decimal_places=2"
            )
        },
    )
    in_stock = models.BooleanField(
        default=True,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product stock available"),
        help_text=_("format: true=available, false=sold-out"),
    )
    is_active = models.BooleanField(
        default=True,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product is active"),
        help_text=_("format: true=active, false=inactive"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("product created"),
        help_text=date_help,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        editable=True,
        verbose_name=_("product last updated"),
        help_text=date_help,
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=max200_help,
    )
    objects = models.Manager()
    available_items = AvailableItemsManager()

    class Meta:
        """
        The product item meta.
        Vobose_name is the name of the model in the admin.
        Vobose_name_plural is the name of the model in the admin.
        ordering is the order in which the items are displayed.
        """

        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def get_product_detail_url(self):
        """
        Return the url for the product detail page.
        """
        return reverse("product-detail", args=[self.slug])

    def __str__(self):
        """
        Returns the name of the product.
        as the primary identification.
        """
        return self.name

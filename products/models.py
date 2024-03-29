from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from products.convert_image import Convert2jpg, Convert2webp

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
            "These are the keywords that your site can be searched "
            "with on Google. Make these single words, relevant to "
            "your site, often searched"
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
        max_length=300,
        unique=False,
        null=False,
        blank=False,
        verbose_name=("product keywords"),
        help_text=(
            "format: required, These are used by Google to "
            "search for the product."
            "These are words that are relevant to the product "
            "and will be added to the Product Name,"
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
        null=False,
        blank=True,
        default="images/default/default_image.png",
        verbose_name=(
            "Product Image - fallback jpeg image, the preferred image is \
                created from this image"
        ),
    )
    image_preferred = models.ImageField(
        upload_to="images/products/",
        null=False,
        blank=False,
        default="images/default/default_image.png",
        verbose_name=(
            "WEBP Product Image - may not show on older devices,  \
            so jpg is fallback image"
        ),
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
    inventory = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name=("product stock level"),
        help_text=("format: required, max_length: 3"),
    )
    in_stock = models.BooleanField(
        default=False,
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
    slug = models.SlugField(
        max_length=200,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=max200_help,
    )
    objects = models.Manager()
    available_items = AvailableItemsManager()

    def save(self, *args, **kwargs):
        if self.image:
            """
            Take the uploaded image and convert it to jpeg and webp.
            """
            saveName = f'{self.name}"_"{self.sku}'
            saveName = saveName.replace(" ", "_")
            # lkm-creation_SaveName_date
            # (lkm-creation, date and extension are
            # handled by the function)
            Convert2webp(self, saveName)
            Convert2jpg(self, saveName)
        # uses the name field to create a slug
        # and saves to the slug field
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

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

    def has_inventory(self):
        return self.inventory > 0

    def remove_items_from_inventory(self, count, save=True):
        """
        Take the input count and subtract it from the inventory.
        If save is true, save the inventory.
        """
        current_inv = self.inventory
        current_inv -= count
        self.inventory = current_inv
        if save:
            self.save()
        return self.inventory

    def update_if_in_stock(self, save=True):
        """
        Check if the inventory is less than or equal to zero.
        If so, set the in_stock flag to false.
        """
        if self.inventory <= 0:
            self.in_stock = False
        if save:
            self.save()
        return self.in_stock

    def __str__(self):
        """
        Returns the name of the product.
        as the primary identification.
        """
        return self.name

    def get_review_average_rating(self):
        """
        Returns the average rating of the product.
        """
        reviews_total = 0
        for review in self.reviews.all():
            reviews_total += review.rating
        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        return 0

    def get_review_count(self):
        """
        Returns the review count of the product.
        """
        return self.reviews.count()

    def get_review_highest_rating(self):
        """
        Returns the review highest rating of the product.
        """
        return self.reviews.aggregate(max_rating=Max("rating"))[
            "max_rating"
        ]


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=5)
    content = models.TextField(max_length=500)
    created_by = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="images/reviews/",
        null=False,
        blank=True,
        verbose_name=(
            "Product Image - fallback jpeg image, the preferred image is \
            created from this image"
        ),
    )
    image_preferred = models.ImageField(
        upload_to="images/reviews/",
        null=False,
        blank=True,
        verbose_name=(
            "WEBP Review Image - may not show on older devices,  \
            so jpg is fallback image"
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the name of the review.
        as the primary identification.
        """
        return f'{self.created_by} " review of" {self.product}'

    def save(self, *args, **kwargs):
        if self.image:
            """
            Take the uploaded image and convert it to jpeg and webp.
            """
            saveName = f'{self.created_by}"_"{self.product}"_review"'
            saveName = saveName.replace(" ", "_")
            # lkm-creation_SaveName_date
            # (lkm-creation, date and extension are
            # handled by the function)
            Convert2webp(self, saveName)
            Convert2jpg(self, saveName)
        super(Review, self).save(*args, **kwargs)

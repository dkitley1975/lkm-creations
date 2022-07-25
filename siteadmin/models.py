import datetime
from io import BytesIO

from django.core.files.base import ContentFile
from django.db import models
from PIL import Image

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
        default="images/default/default_image.png",
        verbose_name=("Home Page Image "),
        help_text=(
            "format: required, 900px by 600px PNG file  \
                   with a transparent background"
        ),
    )
    image_preferred = models.ImageField(
        upload_to="images/homepage/",
        null=False,
        blank=False,
        default="images/default/default_image.png",
        verbose_name=(
            "WEBP Product Image - may not show on older devices,  \
            so jpg is fallback image"
        ),
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

    def save(self, *args, **kwargs):
        if self.image:
            """
            Take the uploaded image and convert it to png and webp.
            """
            self.Convert2webp()
            self.Convert2png()

        super(SiteInfo, self).save(*args, **kwargs)

    def Convert2png(self):
        """
        Convert the image to a png file.
        """
        Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
        convert2png_filename = (
            "%s.png"
            % f'"lkm-creations_home_page_image_"{str(Current_Date)}'
        )  # create a filename
        convert2png_image = Image.open(self.image)
        convert2png_image.thumbnail((900, 600))
        convert2png_image_io = BytesIO()
        convert2png_image.save(
            convert2png_image_io, format="PNG", quality=100
        )
        self.image.save(
            convert2png_filename,
            ContentFile(convert2png_image_io.getvalue()),
            save=False,
        )

    def Convert2webp(self):
        """
        Convert the image to webp format and save it to the database.
        """
        Current_Date = datetime.datetime.today().strftime("%d-%b-%Y")
        convert2webp_filename = (
            "%s.webp"
            % f'"lkm-creations_home_page_image_"{str(Current_Date)}'
        )
        convert2webp_image = Image.open(self.image)
        convert2webp_image.thumbnail((900, 600))
        convert2webp_image_io = BytesIO()
        convert2webp_image.save(
            convert2webp_image_io, format="WEBP", quality=90
        )
        self.image_preferred.save(
            convert2webp_filename,
            ContentFile(convert2webp_image_io.getvalue()),
            save=False,
        )

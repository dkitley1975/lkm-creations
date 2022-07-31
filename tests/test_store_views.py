from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from products.models import Category, Colour, Product
from store.views import products_on_sale, store_front
from siteadmin.models import SiteInfo


class TestViewResponses(TestCase):
    def setUp(self):
        """
        Set up the test data for the test case.
        """
        self.c = Client()
        Category.objects.create(name="test category", slug="test-category")
        Colour.objects.create(name="test colour", slug="test-colour")
        SiteInfo.objects.create(
            alert_message= "We are closed for 1 week, you can still purchase, but we will ship your order on the first day back.",
            image= "images/homepage/lkm-creations_home_page_image_25-Jul-2022.png",
            image_preferred= "images/homepage/lkm-creations_home_page_image_25-Jul-2022.webp",
            image_alt_text= "Amigurumi Crochet Doll of Her Royal Highness and a Corgi",
            store_description= "LKM Creations, Handmade Amigurumi Crochet creations, with a sale on octopus toys mimic umbilical cords, creating a sense of calm that comforts preemie babies.",
            store_keywords= "Handmade, Handcrafted, Custom, Beautiful, Gifts, Presents, Amigurumi Dolls, Amigurumi Toys, Amigurumi Decorative, Amigurumi Gifts, Knitted Dolls, Knitted Toys, Knitted Gifts, Crochet Dolls, Crochet Toys, Crochet Gifts, Animal, Teddy, Dolls, Teddy Bear, Fish, Whales, Octopus,",
            free_delivery_over= "19.99",
            delivery_cost_price= "4.00",
            delivery_price= "7.00",
            phone_number= "07739792514",
            email_address= "lkm-creations@kitley-mcnamara.com",
            is_active= "True",
            facebook_url= "https://www.facebook.com/lkm-creations",
            linkedin_url= "http://www.linkedin.com/in/david-kitley-mcnamara",
            github_url= "https://github.com/dkitley1975",
            twitter_url= "https://twitter.com/McnamaraKitley"
            )

        User.objects.create(username="admin")
        self.testdata1 = Product.objects.create(
            sku=1234567,
            name="test product",
            category_id=1,
            colour_id=1,
            description="test description",
            keywords="test keywords1, test keywords2",
            is_washable="True",
            image="images/default/default_image.png",
            image_alt_text="test image alt text",
            weight="200",
            size="32",
            unit_cost_price="4.25",
            retail_price="10.99",
            sale_price="8.99",
            in_stock="True",
            is_active="True",
            slug="test-product",
        )

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse("category-list", args=["test-category"])
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse("product-detail", args=["test-product"])
        )
        self.assertEqual(response.status_code, 200)

    def test_store_front_html(self):
        """
        Test the home page html.
        @returns None
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = store_front(request)
        html = response.content.decode("utf8")
        self.assertEqual(response.status_code, 200)

    def test_products_on_sale_url(self):
        """
        Test the sale products url.
        """

        response = self.c.get(reverse("sale"))
        self.assertEqual(response.status_code, 200)

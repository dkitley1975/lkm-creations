from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from products.models import Category, Colour, Product
from store.views import products_on_sale, store_front


class TestViewResponses(TestCase):
    def setUp(self):
        """
        Set up the test data for the test case.
        """
        self.c = Client()
        Category.objects.create(name="test category", slug="test-category")
        Colour.objects.create(name="test colour", slug="test-colour")

        User.objects.create(username="admin")
        self.testdata1 = Product.objects.create(
            sku=1234567,
            name="test product",
            category_id=1,
            colour_id=1,
            description="test description",
            keywords="test keywords1, test keywords2",
            is_washable="True",
            image="test_image.jpg",
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
            reverse("store:category-list", args=["test-category"])
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse("store:product-detail", args=["test-product"])
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
        self.assertIn("<title>LKM Creations</title>", html)
        self.assertEqual(response.status_code, 200)

    def test_products_on_sale_url(self):
        """
        Test the sale products url.
        """

        response = self.c.get(reverse("store:sale-products"))
        self.assertEqual(response.status_code, 200)

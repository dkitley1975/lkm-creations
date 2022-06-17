from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from products.models import Category, Colour, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        """
        Create a test category for the test.
        """
        self.testdata1 = Category.objects.create(
            name="test category",
            slug="test-category",
        )

    def test_category_model_entry(self):
        """
        Tests that
        def __str__(self):
        return self.name
        matches the test datas name.

        """
        data = self.testdata1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "test category")


class TestColourModel(TestCase):
    def setUp(self):
        """
        Create a test colour for the test.
        """
        self.testdata1 = Colour.objects.create(
            name="test colour",
            slug="test-colour",
        )

    def test_colour_model_entry(self):
        """
        Tests that
        def __str__(self):
        return self.name
        matches the test datas name.
        """
        data = self.testdata1
        self.assertTrue(isinstance(data, Colour))
        self.assertEqual(str(data), "test colour")


class TestProductsModel(TestCase):
    def setUp(self):
        """
        Set up the test data for the test.
        This is called before every test.
        """
        Category.objects.create(name="test category", slug="test-category")
        Colour.objects.create(name="test colour", slug="test-colour")

        User.objects.create(username="admin")
        self.testdata1 = Product.objects.create(
            name="test product",
            sku=1234567,
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
        self.testdata2 = Product.objects.create(
            name="test product 2",
            sku=1234569,
            category_id=1,
            colour_id=1,
            description="test description 2",
            keywords="test keywords3, test keywords4",
            is_washable=True,
            image="test_image2.jpg",
            image_alt_text="test image alt text2",
            weight="100",
            size="30",
            unit_cost_price="4.50",
            retail_price="12.99",
            sale_price="9.99",
            in_stock=True,
            is_active=True,
            slug="test-product-2",
        )

    def test_products_model_entry(self):
        """
        Tests that
        def __str__(self):
        return self.name
        matches the test datas name.
        """
        data = self.testdata1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "test product")

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.testdata1
        url = reverse("product-detail", args=[data.slug])
        self.assertEqual(url, "/test-product/")
        response = self.client.post(
            reverse("product-detail", args=[data.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        data = self.testdata1
        response = self.client.get(
            reverse("product-detail", args=["test-product"])
        )
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.available_items.all()
        self.assertEqual(data.count(), 2)

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from tomlkit import boolean

from products.models import Category, Colour, Product
from siteadmin.models import SiteInfo


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
            name="test product",
            sku=1234567,
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
            in_stock=True,
            is_active=True,
            slug="test-product",
            inventory=1,
        )
        self.testdata2 = Product.objects.create(
            name="test product 2",
            sku=1234569,
            category_id=1,
            colour_id=1,
            description="test description 2",
            keywords="test keywords3, test keywords4",
            is_washable=True,
            image="images/default/default_image.png",
            image_alt_text="test image alt text2",
            weight="100",
            size="30",
            unit_cost_price="4.50",
            retail_price="12.99",
            sale_price="9.99",
            in_stock=True,
            is_active=True,
            slug="test-product-2",
            inventory="2",

        )

    def test_products_model_entry(self):
        """
        Tests that
        def __str__(self):
        return self.name
        matches the test datase name.
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
        self.assertEqual(url, "/store/test-product/")

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.available_items.all()
        self.assertEqual(data.count(), 2)

    def test_product_inventory(self):
        """
        Test the Product class.
        """
        testdata1 = self.testdata1
        self.assertTrue(isinstance(testdata1, Product))
        self.assertEqual(int(testdata1.inventory), 1)
        self.assertEqual(testdata1.in_stock, True)
        testdata1.inventory = testdata1.inventory - 1
        if self.testdata1.inventory <= 0:
            self.testdata1.in_stock = False
        self.assertEqual(int(testdata1.inventory), 0)
        self.assertEqual(testdata1.in_stock, False)



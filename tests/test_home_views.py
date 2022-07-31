from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from home.views import index
from products.models import Product
from siteadmin.models import SiteInfo


class TestHomeViewResponses(TestCase):
    def setUp(self):
        """
        Set up the client for the network.
        This is necessary for the network to be able
        to connect to the server.
        """
        self.c = Client()
        User.objects.create(username="admin")
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


    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get("/", HTTP_HOST="incorrectaddress.com")
        self.assertEqual(response.status_code, 400)
        # TODO change allowed hosts to the heroku site name once uploaded
        response = self.c.get("/", HTTP_HOST="127.0.0.1:8000")
        self.assertEqual(response.status_code, 200)

    def test_index_url(self):
        """
        Test index response status
        """
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

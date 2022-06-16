from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from home.views import index
from products.models import Product


class TestHomeViewResponses(TestCase):
    def setUp(self):
        """
        Set up the client for the network. This is necessary for the network to be able to connect to the server.
        """
        self.c = Client()
        User.objects.create(username="admin")

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

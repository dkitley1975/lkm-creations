from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from products.models import Category, Product


class ProductSitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the products.
    """

    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Product.available_items.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return "/store/%s" % (obj.slug)


class CategorySitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the categories.
    """

    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return "/store/category/%s" % (obj.slug)


class StaticSitemap(Sitemap):
    """
    Add to the sitemap for the website.
    This adds a list of all the main static pages with important content.
    """

    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            "home:home",
            "home:privacy-policy",
            "home:terms-of-service-policy",
            "home:returns-policy",
            "home:disclaimer-policy",
            "home:shipping-policy",
            "home:cookie-policy",
        ]

    def location(self, item):
        return reverse(item)

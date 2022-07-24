from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from core.views import robots_txt, bad_request_error_400, forbidden_error_403, page_not_found_view_404, internal_error_500

from .sitemaps import CategorySitemap, ProductSitemap, StaticSitemap

sitemaps = {
    "products": ProductSitemap,
    "static": StaticSitemap,
    "categories": CategorySitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls", namespace="home")),
    path("dashboard/", include("profiles.urls")),
    path("store/", include("store.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("product/", include("products.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", robots_txt),
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("webmanifest/favicons/favicon.ico")
        ),
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


handler400 = "core.views.bad_request_error_400"
handler403 = "core.views.forbidden_error_403"
handler404 = "core.views.page_not_found_view_404"
handler500 = "core.views.internal_error_500"

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls", namespace="home")),
    path("store/", include("store.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
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

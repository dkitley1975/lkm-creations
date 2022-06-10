from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls", namespace="home")),
    path("", include("store.urls", namespace="store")),
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("webmanifest/favicons/favicon.ico")
        ),
    ),
]

from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("siteadmin.urls")),
    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("webmanifest/favicons/favicon.ico")
        ),
    ),
]

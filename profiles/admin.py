from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = "User Address"
    fk_name = "user"
    fieldsets = (
        (
            "Address",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "default_street_address1",
                    "default_street_address2",
                    "default_town_or_city",
                    "default_county",
                    "default_country",
                    "default_postcode",
                    "default_phone_number",
                ),
            },
        ),
    )


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    verbose_name = "User Details"
    extra = 1
    fieldsets = (
        (
            "Personal info",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
        (
            "Password info",
            {
                "classes": ("collapse", "extrapretty"),
                "fields": ("password",),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = (
        "username",
        "email",
    )


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Create a new config object.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "checkout"

    def ready(self):
        pass

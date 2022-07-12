from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Create a new config object.
    """
    name = "checkout"

    def ready(self):
        import checkout.signals

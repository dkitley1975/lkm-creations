from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from checkout.models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total each time a lineitem is amended
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total each time a lineitem is deleted
    """
    instance.order.update_total()

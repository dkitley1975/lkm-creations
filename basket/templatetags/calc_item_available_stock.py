from django import template

register = template.Library()


@register.filter(name="calc_item_available_stock")
def calc_item_available_stock(inventory, item_inventory):
    return inventory - item_inventory

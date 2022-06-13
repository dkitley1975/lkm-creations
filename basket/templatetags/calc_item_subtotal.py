from django import template

register = template.Library()


@register.filter(name="calc_item_subtotal")
def calc_item_subtotal(unit_price, quantity):
    return unit_price * quantity

from django.shortcuts import get_object_or_404

from products.models import Product
from siteadmin.models import SiteInfo


def basket_contents(request):
    basket_items = []
    subtotal = 0
    total_quantity = 0
    delivery_charge = 0

    free_delivery_threshold = (
        SiteInfo.objects.all()
        .filter(is_active=True)
        .order_by("-created_at")[0]
        .free_delivery_over
    )
    default_delivery_price = (
        SiteInfo.objects.all()
        .filter(is_active=True)
        .order_by("-created_at")[0]
        .delivery_price
    )

    basket = request.session.get("basket", {})

    for item_id, quantity in basket.items():
        """
        For each item in the basket,
        get the product,
        and add the quantity and price to the total.
        @param basket - the basket dictionary
        @returns the total price and the product count
        """
        product = get_object_or_404(Product, pk=item_id)
        if product.sale_price is not None and product.sale_price > 0:
            unit_price = product.sale_price
        else:
            unit_price = product.retail_price
        session_item_inventory = product.inventory
        session_item_inventory -= quantity
        subtotal += quantity * unit_price
        total_quantity += quantity
        basket_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
                "unit_price": unit_price,
                "session_item_inventory":session_item_inventory,
            }
        )
        print( basket_items)
    if subtotal < free_delivery_threshold:
        delivery_charge = default_delivery_price
        spend4free_delivery = free_delivery_threshold - subtotal
    else:
        delivery_charge = 0
        spend4free_delivery = 0
    grand_total = subtotal + delivery_charge
    context = {
        "basket_items": basket_items,
        "subtotal": subtotal,
        "total_quantity": total_quantity,
        "delivery_charge": delivery_charge,
        "spend4free_delivery": spend4free_delivery,
        "free_delivery_threshold": free_delivery_threshold,
        "grand_total": grand_total,
    }

    return context

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from plans.models import Subscribe

from products.models import Product


def bag_contents(request):

    bag_items = []
    plan_items = []

    total = 0
    product_count = 0
    total_plan = 0
    plan_count = 0

    bag = request.session.get('bag', {})
    plan_bag = request.session.get('plan_bag', {})

    for item_id, item_data in bag.items():

        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
            
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    for plan_id, plan_data in plan_bag.items():
        plan = get_object_or_404(Subscribe, pk=plan_id)
        total_plan += plan_data['quantity'] * plan.price
        plan_count += plan_data['quantity']
        plan_items.append({
            'plan_id': plan_id,
            'quantity': plan_data['quantity'],
            'plan': plan,
            'duration_weeks': plan.duration_weeks,
            'level': plan.level,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'plan_count': plan_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

from django import template
from django.db.models import Count, Q
from datetime import datetime, timedelta

from ..models import Product


register = template.Library()

@register.filter
def popular_products():
    last_month = datetime.today() - timedelta(days=30)
    
    return {
        "popular_products" : Product.objects.published().annotate(count=Count('visit', filter=Q(productvisits__datetime_created__gt=last_month)))
        .order_by('-count', '-published')
    }


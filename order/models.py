from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("user"))
    
    first_name = models.CharField(_("first name"), max_length=100)
    
    last_name = models.CharField(_("last name"), max_length=100)
    
    phone = models.CharField(_("phone number"), max_length=20)

    address = models.TextField(_("address"))
    
    note = models.CharField(_("note"), max_length=200, blank=True)
    
    zarinpal_authority = models.CharField(_("zarinpal_authority"), max_length=225, blank=True)
    zarinpal_ref_id = models.CharField(_("zarinpal_ref_id"), max_length=150, blank=True)
    zarinpal_data = models.TextField(_("zarinpal_data"), blank=True)
    
    is_paid = models.BooleanField(_("paid"), default=False)
    
    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())
    
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("order"), related_name="items")
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"), related_name="order")
    
    quantity = models.PositiveIntegerField(_("quantity"), default=1)
    
    price = models.PositiveIntegerField(_("price"))
    
    def __str__(self):
        return f'Order {self.order} : Product {self.product}'
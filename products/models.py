from audioop import reverse
from django.db import models

from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('product name'))
    description = models.TextField(_('product description'))
    price = models.PositiveIntegerField(_('product price'), default=0)
    
    image = models.ImageField(_('product image'), upload_to='products/product_image/')
    
    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)
    
    is_active = models.BooleanField(_('is_active'), default=True)

    def __str__(self):
        return f'product name:{self.name} product is_active : {self.is_active}'
    
    # def get_absolute_url(self):
    #     return reverse('product_details', args=[self.product_id])
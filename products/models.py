from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('product name'))
    description = models.TextField(_('product description'))
    price = models.PositiveIntegerField(_('product price'), default=0)
    
    image = models.ImageField(_('product image'), upload_to='products/product_image/')
    
    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now())
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)
    
    is_active = models.BooleanField(_('is_active'), default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product:product_details', args=[self.pk])
    
class Comment(models.Model):
    STARS_CHOICES=[
        ('1', _('awful')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect')),
    ]
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'), related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'), related_name='comments')
    
    text = models.TextField(_('text'))
    stars = models.CharField(choices=STARS_CHOICES, max_length=10, verbose_name=_('stars'),)
    
    datetime_created = models.DateTimeField(_('Date time created'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
        
    active = models.BooleanField(default=True)
  
    def __str__(self):
        return str(self.product)
    
    def get_absolute_url(self):
        return reverse('product:product_details', args=[self.product.id ])

    
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name="children", verbose_name=_('category_parent'), on_delete=models.SET_NULL)
    
    title = models.CharField(_('title'), max_length=200)
    
    slug = models.SlugField(_('slug'), unique=True, max_length=250)
    
    status = models.BooleanField(_('status'), default=True)

    position = models.IntegerField(_('position'))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('parent__id', 'position')
    
    def __str__(self):
        return self.title

    objects = CategoryManager()


class ProductManager(models.Manager):
    def published(self):
        return self.filter(is_active=True).order_by('published')


class Product(models.Model):
    
    name = models.CharField(_('product name'), max_length=200 )
    
    slug = models.CharField(_('slug'), max_length=200, unique=True)
    
    category = models.ManyToManyField(Category, verbose_name=_('Category'), related_name="products")

    description = RichTextField(_('description'))
    
    price = models.PositiveIntegerField(_('product price'), default=0)
    
    image = models.ImageField(_('product image'), upload_to='products/product_image/')

    published = models.DateTimeField(_('published'), default=timezone.now())
    
    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)
    
    is_active = models.BooleanField(_('is_active'), default=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('published',)

    # Django functions 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        We use this method to get the absolute url for the product.
        """
        return reverse('product:product_details', args=[self.slug])
       
    # My functions 
        
    def categories_to_string(self):
        """
        We use the following function to convert a list of categories to a string.
        """
        return " , ".join([category.title for category in self.category.active()])
    categories_to_string.short_description = _('Categories')

    objects = ProductManager()
    


class CommentManager(models.Manager):
    def active(self):
        return self.filter(active=True).order_by('datetime_created')

    
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
  
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('datetime_created',)

  
    def __str__(self):
        return str(self.product)
    
    def get_absolute_url(self):
        return reverse('product:product_details', args=[self.product.id ])

    objects = CommentManager()
    


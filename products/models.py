from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from visits.models import IPAddress

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

 
class Color(models.Model):
    name = models.CharField(_('color name'), max_length=200 )
    
    hex_code = models.CharField(_('color hex code'), max_length=6)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ('name',)
    
    def __str__(self):
        return self.name

 
class Size(models.Model):
    size_number = models.CharField(_('size number'), max_length=200 )
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')
        ordering = ('size_number',)
    
    def __str__(self):
        return self.size_number
  
 

class Product(models.Model):
    
    name = models.CharField(_('product name'), max_length=200 )
    
    slug = models.CharField(_('slug'), max_length=200, unique=True)
    
    category = models.ManyToManyField(Category, verbose_name=_('Category'), related_name="products")

    description = RichTextField(_('description'))
    
    price = models.PositiveIntegerField(_('product price'), default=0)
    
    image = models.ImageField(_('product image'), upload_to='products/product_image/')
    
    colors = models.ManyToManyField(Color, verbose_name=_('colors'), related_name="products")
    
    sizes = models.ManyToManyField(Size, verbose_name=_('sizes'), related_name="products")

    published = models.DateTimeField(_('published'), default=timezone.now())
    
    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)
    
    is_active = models.BooleanField(_('is_active'), default=True)
    
    visit = models.ManyToManyField(IPAddress, through="ProductVisits", blank=True, related_name='visit', verbose_name=_('visit'))

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

        
    # def visits_to_string(self):
    #     """
    #     We use the following function to convert a list of visits to a string.
    #     """
    #     return " , ".join([number_of_visit for number_of_visit in len(self.visit)])
    # visits_to_string.short_description = _('visit')


    def colors_to_string(self):
        """
        We use the following function to convert a list of colors to a string.
        """
        return " , ".join([color.name for color in self.colors.all()])
    colors_to_string.short_description = _('colors')


    def sizes_to_string(self):
        """
        We use the following function to convert a list of sizes to a string.
        """
        return " , ".join([color.size_number for color in self.sizes.all()])
    sizes_to_string.short_description = _('sizes')

    objects = ProductManager()
    


class ProductSizeColor(models.Model):
    COLOR_CHOICES=[
        ('قرمز', _('red')),
        ('آبی', _('blue')),
        ('مشکی', _('black')),
        ('طوسی', _('gray')),
        ('سبز', _('green')),
    ]    
    
    SIZE_CHOICES=[
        ('بزرگ', _('big')),
        ('متوسط', _('normal')),
        ('کوچیک', _('small')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size_color', verbose_name='product_size_color')
    
    color = models.CharField(_('color'), max_length=250, choices = COLOR_CHOICES)
    
    size = models.CharField(_('size'), max_length=100, choices = SIZE_CHOICES)



class ProductVisits(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    
    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
   

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
    


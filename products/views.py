from django.shortcuts import render
from django.views import generic

from .models import Product

class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    

class ProductDetailsView(generic.DetailView):
    model = Product
    template_name = 'products/product_details.html'

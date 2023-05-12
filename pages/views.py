from django.shortcuts import render
from django.views import generic

from products.models import Product

class HomePageView(generic.ListView):
    template_name = 'home.html'
    model = Product 
    context_object_name = 'products'


class ProfilePageView(generic.TemplateView):
    template_name = 'pages/profile.html'



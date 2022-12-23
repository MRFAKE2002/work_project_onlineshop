from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details_page_view, name='cart_details_page'),
]

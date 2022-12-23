from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details_page_view, name='cart_details_page'),
    path('add_to_cart/<int:product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
]

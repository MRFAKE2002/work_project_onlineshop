from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order_created_view, name='order_created'),
]

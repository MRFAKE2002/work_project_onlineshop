from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailsView.as_view(), name='product_details'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
]

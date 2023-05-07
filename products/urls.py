from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', views.ProductDetailsView.as_view(), name='product_details'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('category/<slug:slug>/', views.categories_page_view, name='categories'),
]

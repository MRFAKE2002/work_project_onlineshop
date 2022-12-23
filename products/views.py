from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import CommentForm
from .models import Product, Comment
from cart.forms import AddProductToCartForm

class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(is_active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    

class ProductDetailsView(generic.DetailView):
    model = Product
    template_name = 'products/product_details.html'
    
    def get_context_data(self, **kwargs):
        # This code is default in django for get Product and Comment form model
        context = super().get_context_data(**kwargs)
        # We use this code to add CommentForm in the context and use it in our product_detail
        context['comment_form'] = CommentForm()
        # # We use this code to add ProductAddToCartForm in the context and use it in our product_detail        
        context['add_cart_form'] = AddProductToCartForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
        
    def form_valid(self, form):
        
        user_comment = form.save(commit=False)
        
        user_comment.user = self.request.user
        
        # For get the comment product we must get the product id from the url that we POST the " product.id " by comment that user send it
        product_id = int(self.kwargs['product_id'])
        
        product = get_object_or_404(Product, id=product_id)
        
        user_comment.product = product
        
        user_comment.save()
        
        return super().form_valid(form)
    

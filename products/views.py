from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CommentForm
from .models import Product, Comment, Categories
from cart.forms import AddProductToCartForm
from cart.cart import Cart

def categories_page_view(request, slug):
    try:
        categories_products = get_object_or_404(Product, slug=slug)
    except :
        return redirect("home")
    
    return render(request, 'categories.html', {'categories_products': categories_products})


# class CategoriesPageViews(generic.ListView):
#     queryset = Product.objects.filter(is_active=True)
#     template_name = 'categories.html'


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
        
        # context['cart'] = Cart()
        
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
        
        messages.success(self.request, _('Comment created successfully.'))
        
        return super().form_valid(form)
    

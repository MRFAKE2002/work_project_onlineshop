from typing import Any
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import Q

from .forms import CommentForm
from .models import Product, Comment, Category
from cart.forms import AddProductToCartForm
from cart.cart import Cart


# Create Your categories_page_view By Functional.
def categories_page_view(request, slug, page=1):
    try:
        category = get_object_or_404(Category.objects.active(), slug=slug)
    except :
        return redirect("home")
    
    product_list = category.products.published()
    
    paginator = Paginator(product_list, 4)
    
    products = paginator.get_page(page)
    
    context = {
        'category': category,
        'products': products
    }
    
    return render(request, 'categories.html', context)


# Create Your CategoriesPageViews By classbased.
# class CategoriesPageViews(generic.ListView):
#     queryset = Product.objects.published()
    
#     template_name = 'categories.html'
    
#     paginate_by = 4


# --------------------------------------------------------------------------------------- #

# Create Your product_list_view By Functional.
# def product_list_view(request, page=1):
#     product_list = Product.objects.published()
    
#     paginator = Paginator(product_list, 6)
    
#     products_in_page = paginator.get_page(page)
    
#     context = {'products':products_in_page}
    
#     return render(request, 'products/product_list.html', context)
    

# Create Your ProductListView By classbased.
class ProductListView(generic.ListView):
    queryset = Product.objects.published()
    
    template_name = 'products/product_list.html'
    
    context_object_name = 'products' # default object_list
    
    paginate_by = 6


# --------------------------------------------------------------------------------------- #

# Create Your product_detail_view By functional.
# def product_detail_view(request, slug):
#     context = {
#         "product" : get_object_or_404(Product.objects.published(), slug=slug),
#     }

#     return render(request, 'products/product_details.html', context)


# Create Your ProductDetailView By classbased.
class ProductDetailsView(generic.DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
    
        product = get_object_or_404(Product.objects.published(), slug=slug)
    
        ip_address = self.request.user.ip_address
        if ip_address not in product.visit.all():
            product.visit.add(ip_address)
        
        return product
    
    template_name = 'products/product_details.html'
    
    def get_context_data(self, **kwargs):
        # This code is default in django for get Product and Comment form model
        context = super().get_context_data(**kwargs)
        # We use this code to add CommentForm in the context and use it in our product_detail
        context['comment_form'] = CommentForm()
        # # We use this code to add ProductAddToCartForm in the context and use it in our product_detail        
        context['add_cart_form'] = AddProductToCartForm()
                
        return context

# --------------------------------------------------------------------------------------- #

# Create Your CommentCreateView By classbased.
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
    

# --------------------------------------------------------------------------------------- #

# Create Your ProductSearchListView By classbased.
class ProductSearchListView(generic.ListView):
    paginate_by = 2
    template_name = 'products/search_list.html'
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Product.objects.filter(Q(description__icontains=search) | Q(name__icontains=search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search = self.request.GET.get('q')
        
        context['search'] = search
        
        context['products'] = Product.objects.filter(Q(description__icontains=search) | Q(name__icontains=search))
        
        return context



# # Create Your search_product_list By functional.
# def search_post(request):
#     if request.method == 'POST':
#         search_query = request.POST['search_query']
#         products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
#         return render(request, 'app/template_name.html', {'query':search_query, 'products':products})
#     else:
#         return render(request, 'app/template_name.html',{})


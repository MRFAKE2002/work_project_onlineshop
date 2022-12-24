from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddProductToCartForm
from products.models import Product

def cart_details_page_view(request):
    """
    We use this function for make a cart_detail page.
    """
    cart = Cart(request)
    
    return render(request, 'cart/cart_detail_page.html', {'cart' : cart})

def add_product_to_cart(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    form = AddProductToCartForm(request.POST)
    
    if form.is_valid():
        cleaned_data = form.cleaned_data
        
        quantity = int(cleaned_data['quantity'])
        
        cart.add(product, quantity)
        
    return redirect("cart:cart_details_page")

def remove_product_from_cart_view(request, product_id):
    """
    We use this function for remove the product from the cart by GET request in cart_detail page
    """
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)
    
    return redirect('cart:cart_detail')

def clear_cart_view(request):
    """
    We use this function to clear the cart by form in cart_detail page
    """
    cart = Cart(request)
    
    cart.clear()

    return redirect('cart:cart_detail')

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import AddProductToCartForm
from products.models import Product

def cart_details_page_view(request):
    """
    We use this function for make a cart_detail page.
    """
    cart = Cart(request)
    
    for product in cart:
        product['product_inplace_current_quantity'] = AddProductToCartForm(initial={
            'quantity' : product['quantity'],
            'inplace' : True
        })
    
    return render(request, 'cart/cart_detail_page.html', {'cart' : cart})

@require_POST
def add_product_to_cart(request, product_id):
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    form = AddProductToCartForm(request.POST)
    
    if form.is_valid():
        cleaned_data = form.cleaned_data
        
        quantity = int(cleaned_data['quantity'])
        
        replace_current_price = cleaned_data['inplace']
        
        cart.add(product, quantity, replace_current_price)
        
    return redirect("cart:cart_details_page")

@require_POST
def remove_product_from_cart_view(request, product_id):
    """
    We use this function for remove the product from the cart by GET request in cart_detail page
    """
    cart = Cart(request)
    
    product = get_object_or_404(Product, id=product_id)
    
    cart.remove(product)
    
    return redirect('cart:cart_details_page')

def clear_cart_view(request):
    """
    We use this function to clear the cart by form in cart_detail page
    """
    cart = Cart(request)
    
    cart.clear()

    return redirect('cart:cart_details_page')

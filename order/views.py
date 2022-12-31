from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import OrderItems
from cart.cart import Cart
from products.models import Product

@login_required
def order_created_view(request):
    form = OrderForm()
    
    cart = Cart(request)
        
    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            for item in cart:
                OrderItems.objects.create(
                    order = order,
                    product = item['product_info'],
                    quantity = item['quantity'],
                    price = item['product_info'].price,
                )
            
            cart.clear()
    
    return  render(request, 'order/order_created.html', {
        'form': form,
    })
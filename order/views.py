from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import OrderItems
from cart.cart import Cart

@login_required
def order_created_view(request):
    form = OrderForm()
    
    cart = Cart(request)
    
    if len(cart) == 0:
        
        messages.warning(request, _("You must go shopping at first"))
        
        return redirect('product:product_list')
        
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
            
        request.user.first_name = order.first_name
        request.user.last_name = order.last_name
        request.user.save()
        
        messages.success(request, _("Your order has successfully done"))
        
        return redirect("home")
    
    return  render(request, 'order/order_created.html', {
        'form': form,
    })
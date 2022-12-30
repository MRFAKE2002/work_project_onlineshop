from django.shortcuts import render

def order_created_view(request):
    return  render(request, 'order/order_created/')
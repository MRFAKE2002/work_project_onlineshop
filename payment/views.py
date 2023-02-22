from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
import requests
import json

from order.models import Order

def payment_process_view(request):
    
    order_id = request.session.get('order_id')
    
    order = get_object_or_404(Order, id=order_id)
    
    toman_total_price = order.get_total_price()
    
    rial_total_price = toman_total_price * 10
    
    zarinpal_request_url = ''
    
    request_headers = {
        "accept" : "application/json",
        "content_type" : "application/json",
    }
    
    
    request_data = {
        "merchant_id" : settings.ZARINPAL_MERCHANT_ID,
        "amount" : rial_total_price,
        "description" : f'#{order_id}: {order.first_name} {order.last_name}',
        "callback" : "http://127.0.0.1:8000" + reverse('payment:payment_callback'),
    }
    
    
    response = requests.post(url='', data=json.dumps(request_data), headers=request_headers)
    
    data = response.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()
    
    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('')
    else:
        return HttpResponse('Error from zarinpal')
     
     
def payment_callback_view(request):
    
    payment_authority = request.GET.get('Authority')
    
    payment_status = request.GET.get('Status')
    
    toman_total_price = order.get_total_price()
    
    rial_total_price = toman_total_price * 10
    
    order = get_object_or_404(Order, zarinpal_authority=payment_authority)
    
    if payment_status == 'OK':
        
        request_headers = {
            "accept" : "application/json",
            "content_type" : "application/json",
        }
        
        
        request_data = {
            "merchant_id" : settings.ZARINPAL_MERCHANT_ID,
            "amount" : rial_total_price,
            "authority" : payment_authority,
        }
        
        response = requests.post(url='', data=json.dumps(request_data), headers=request_headers)
        
        if 'data' in response.json() and ('errors' not in response.json()['data'] or len(response.json()['data']['errors'])) == 0:
            data = response.json()['data']
            
            payment_code = data['code']
            
            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = data['ref_id']
                order.zarinpal_data = data
                order.save()
                
                return HttpResponse('تراکنش موفق')

        
        elif payment_code == 101:
            return HttpResponse('اتمام')

        else:
            error_code = response.json()['errors']['code']
            error_message = response.json()['errors']['message']
            return HttpResponse(f'تراکنش ناموفق {error_code} {error_message}')
    
    else:
        return HttpResponse('تراکنش ناموفق')


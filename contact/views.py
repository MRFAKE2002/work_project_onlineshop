from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings

from .forms import ContactUsForm

def contact_us_page(request):
    form = ContactUsForm()
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            
            subject = "Website Inquiry" 
            
            email_from = settings.EMAIL_HOST_USER
			
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email'], 
			'message':form.cleaned_data['message'], 
			}
			
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "mr3fake@gmail.com", ["mr3fake@gmail.com"]) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")

    form = ContactUsForm()  
    return render(request, 'contact/contact.html', {'form': form})

from django.views import generic 

# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.contrib.auth import login, authenticate, get_user_model
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding  import  force_bytes, force_text
# from django.utils.http import  urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader  import  render_to_string
# from django.core.mail import EmailMessage
# from django.utils.translation import ugettext as _

# from .forms import SignUpForm
# from .token import account_activation_token
# from .models import CustomUser


# def signup_view(request):
#     if request.method == 'POST': 
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = _("The activation link has been sent to your email address.")
#             message = render_to_string("account_active_email.html",{user:CustomUser, 
#                                                                 current_site.domain:"domain",
#                                                                 urlsafe_base64_encode(force_bytes(user.pk)):"uid",
#                                                                 account_activation_token.make_token(CustomUser):"token",
#                                                                 })
#             to_email = form.cleaned_data.get("email")
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse(_("Please check your email address to complete the registration."))
#         else:
#             form=SignUpForm()
#             return render(request, "account/signup.html", {form:form}) 

# def active(request, uidb64, token):
#     User = get_user_model()
    
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))  
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist): 
#         user = None
    
#     if user != None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse(_("Thank you for confirming your email."))
#     else:
#         return HttpResponse(_("The activation link is invalid."))


class AdminPageView(generic.TemplateView):
    template_name = 'accounts/admin.html'

 

  

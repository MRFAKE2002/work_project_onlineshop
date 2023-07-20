from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy 
from accounts.models import CustomUser

class UserProfileView(generic.UpdateView):
    model = get_user_model()
    
    fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'city']
    
    success_url = reverse_lazy('profile:profile')

    template_name = 'user_profile/profile.html'
    
    def get_object(self):
        return CustomUser.objects.get(pk = self.request.user.pk)


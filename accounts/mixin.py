from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.utils.translation import gettext_lazy as _

# class ProductAccessMixin():
#     def dispatch(self, request, *args, **kwargs):        
#         if request.user == self.request.user.is_superuser:
#             return super().dispatch(request, *args, **kwargs)
#         else:
#             raise Http404(_(" You can't see this page."))


class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    We use this mixin to access the superuser required for admin pages.
    """
    def test_func(self):
        return self.request.user.is_superuser

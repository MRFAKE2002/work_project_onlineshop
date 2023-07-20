from django.views import generic 
from django.urls import reverse_lazy 

from products.models import Product
from .mixin import SuperUserRequiredMixin

class HomeAdminView(SuperUserRequiredMixin, generic.TemplateView):
    template_name = 'accounts/admin.html'

 
class ProductListAdminView(SuperUserRequiredMixin, generic.ListView):
    queryset = Product.objects.published()
    
    template_name = 'accounts/product_list.html'
    
    context_object_name = "products"
    

class ProductCreatedAdminView(SuperUserRequiredMixin, generic.CreateView):
    model = Product
    
    fields = ["name", "slug", "category", "description", "price", "image", "published", "is_active"]
    
    template_name = "accounts/product_created_update.html"


class ProductUpdatedAdminView(SuperUserRequiredMixin, generic.UpdateView):
    model = Product
    
    fields = ["name", "slug", "category", "description", "price", "image", "published", "is_active"]
    
    template_name = "accounts/product_created_update.html"


class ProductDeletedAdminView(SuperUserRequiredMixin, generic.DeleteView):
    model = Product
    
    template_name = "accounts/product_deleted_admin.html"
    
    success_url = reverse_lazy("accounts:product_list")

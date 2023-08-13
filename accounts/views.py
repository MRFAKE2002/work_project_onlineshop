from django.views import generic 
from django.urls import reverse_lazy 
from django.db.models import Count, Q
from datetime import datetime, timedelta

from products.models import Product
from .mixin import SuperUserRequiredMixin

class HomeAdminView(SuperUserRequiredMixin, generic.TemplateView):
    template_name = 'accounts/admin.html'

 
class ProductListAdminView(SuperUserRequiredMixin, generic.ListView):
    last_month = datetime.today() - timedelta(days=30)
    
    queryset = Product.objects.published().annotate(count=Count('visit', filter=Q(productvisits__datetime_created__gt=last_month))).order_by('-count', '-published')
    
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

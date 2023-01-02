from .models import Product

# We use this function to have access to the cart object in all templates and we must add it in settings TEMPLATES
def products(request):
    return {
        'products' : Product.objects.all(),
        }
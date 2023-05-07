from .models import Product, Category

# We use this function to have access to the cart object in all templates and we must add it in settings TEMPLATES
def products(request):
    return {
        'products' : Product.objects.all(),
        }


# We use this function to set categories title in top header template
def categories(request):
    return {
        'categories' : Category.objects.all(),
        }


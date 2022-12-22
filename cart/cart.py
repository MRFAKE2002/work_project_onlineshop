from django.shortcuts import get_object_or_404

from products.models import Product

class Cart:
    def __init__(self, request):
        """
        Initialize a cart if not existing.
        """
        self.request = request
        
        self.session = request.session
        
        cart = self.session.get('cart')
        
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
        
    def add(self, product, quantity=1):
        """
        Add specified product to cart.
        """
        
        product_id = str(product.id)
                
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}

        self.save()
    def remove(self, product):
        """
        Remove specified product from cart.
        """
        product_id = str(product.id)
        
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.save()
        
    def save(self):
        """
        Mark session as modified to save changes to cart.
        """
        self.session.modified = True
    
    def __init__(self):
        product_id = self.cart.keys()
        
        product_details = Product.objects.filter(id__in=product_id)
        
        cart = self.cart.copy()
        
        for product in product_details:
            cart[str(product.id)]['product_info'] = product
        
        for items in cart.values():
            yield items
    
    def __len__(self):
        return len(self.cart.keys())
        
    def clear(self):
        del self.session['cart']

        self.save()    
    
    def get_total_price(self):
        
        product_id = self.cart.keys()
        
        product_details = Product.objects.filter(id__in=product_id)
        
        return sum(product_info.price for product_info in product_details)

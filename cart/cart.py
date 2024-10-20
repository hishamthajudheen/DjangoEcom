from core.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get current session key
        cart = self.session.get('session_key')
        
        # If new user, create a session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Making cart available on all pages        
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)} 
            self.cart[product_id] = int(product_qty)
                      
        self.session.modified = True

        
    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids) 
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        ourcart = self.cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        return self.cart
    
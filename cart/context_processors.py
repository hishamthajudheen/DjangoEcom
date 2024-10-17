from .cart import Cart

# Creating context processor to make cart work everywhere
def cart(request):    
    return {'cart': Cart(request)}
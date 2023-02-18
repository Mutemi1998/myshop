from .cart import Cart


#add cat to content processors to make it available in all templates
def cart(request):
    return {'cart': Cart(request)}
class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shopping_cart = self.session['shoping_cart']
        if not shopping_cart:
            self.session['shoping_cart']
        
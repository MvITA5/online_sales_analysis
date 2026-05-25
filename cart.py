# cart.py

class Cart:
  def __init__(self):
    self.cart_items = []

  def add_product(self, product):
    self.cart_items.append(product)

  def display_cart(self):
    if not self.cart_items:
      print("Cart is empty.")
    return
    print("Cart Items:")
    for product in self.cart_items:
       product.display_info()

  def total_payment(self):
     total = sum(item.price * item.quantity for item in self.cart_items)
     return total

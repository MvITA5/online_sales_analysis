# product_manager.py

from product import Product

class ProductManager:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def display_products(self):
     if not self.products:
       print("No products available.")
     for product in self.products:
        product.display_info()

  def total_inventory_value(self):
    total = sum(product.price * product.quantity for product in self.products)
    return total

  def remove_product_by_name(self, name):
     original_len = len(self.products)
     self.products = [product for product in self.products if product.name != name]
     if len(self.products) < original_len:
        print(f"Product '{name}' removed.")
     else:
        print(f"Product '{name}' not found.")

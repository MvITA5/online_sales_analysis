# main.py

from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
  pm = ProductManager()

  pm.add_product(Product("Laptop", 1200.00, 5))
  pm.add_product(Product("Mouse", 25.50, 10))
  pm.add_product(Product("Keyboard", 45.99, 7))

  print("Available products:")
  pm.display_products()
  print(f"Total inventory value: ${pm.total_inventory_value():.2f}\n")

  cart = Cart()
  for i in range(min(3, len(pm.products))):
    cart.add_product(pm.products[i])

  print("Shopping Cart:")
  cart.display_cart()
  print(f"Total payment due: ${cart.total_payment():.2f}")

if __name__ == "__main__":
  main()

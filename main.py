# main.py

from product import Product
from product_manager import ProductManager

def main():
  pm = ProductManager()

  pm.add_product(Product("Laptop", 1200.00, 5))
  pm.add_product(Product("Mouse", 25.50, 10))
  pm.add_product(Product("Keyboard", 45.99, 7))

  print("Available products:")
  pm.display_products()
  print(f"Total inventory value: ${pm.total_inventory_value():.2f}\n")

if __name__ == "__main__":
  main()

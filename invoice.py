#Invoice
customer_name=input("Enter customer name:")
product_name=input("Enter product name:")
price=float(input("Enter product price:"))

print("\n-----------INVOICE------------")
print(f"Customer's Name:{customer_name}")
print(f"Product:{product_name}")
print(f"Price:Rs{price:.2f}")
print("---------------------------------")
print("Thank you!")

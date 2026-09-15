"""
Phase 1 - Data Structures: Iterating over Dictionaries
"""

inventory = {
    "Laptop": 12,
    "Mechanical Keyboard": 35,
    "Wireless Mouse": 50,
    "4K Monitor": 8
}

print("=== Iterating Keys ===")
for item_name in inventory.keys():
    print(f"- {item_name}")

print("
=== Iterating Values ===")
total_stock = sum(inventory.values())
print(f"Total units in stock: {total_stock}")

print("
=== Iterating Key-Value Pairs (.items()) ===")
for product, quantity in inventory.items():
    print(f"Product: {product:<20} | In Stock: {quantity:02d}")

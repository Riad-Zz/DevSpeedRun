"""
Phase 1 - Functional Python: Multi-Criteria Sorting with Keys
"""

items = [
    ("Laptop", "Electronics", 1200),
    ("Apple", "Groceries", 2),
    ("Desk", "Furniture", 350),
    ("Smartphone", "Electronics", 800),
    ("Coffee", "Groceries", 15)
]

# Sort by Category, then by Price ascending
items.sort(key=lambda item: (item[1], item[2]))
print("Sorted by Category then Price:")
for name, cat, price in items:
    print(f"  {cat:<15} | ${price:>5} | {name}")

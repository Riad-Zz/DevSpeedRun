"""
Phase 1 - Functional Python: Lambda Expressions
"""

# Single-line anonymous function
add = lambda a, b: a + b
square = lambda x: x ** 2
is_even = lambda n: n % 2 == 0

print(f"add(12, 18) = {add(12, 18)}")
print(f"square(9) = {square(9)}")
print(f"is_even(14) = {is_even(14)}")

# Inline lambda for sorting complex objects
developers = [
    {"name": "Alice", "commits": 140},
    {"name": "Bob", "commits": 85},
    {"name": "Charlie", "commits": 220}
]

developers.sort(key=lambda dev: dev["commits"], reverse=True)
print("Developers sorted by commits:", developers)
assert developers[0]["name"] == "Charlie"

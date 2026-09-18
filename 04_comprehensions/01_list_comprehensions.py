"""
Phase 1 - Comprehensions: List Comprehensions with Filters
"""

raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mapping: squares
squares = [x**2 for x in raw_numbers]
print("Squares:", squares)

# Filtering: even squares only
even_squares = [x**2 for x in raw_numbers if x % 2 == 0]
print("Even squares:", even_squares)

# Conditional expression inside comprehension
labels = ["Even" if x % 2 == 0 else "Odd" for x in raw_numbers]
print("Parity labels:", labels[:5])

# String transformation
modules = ["basics", "loops", "functions", "oop"]
clean_headers = [m.capitalize() for m in modules]
print("Clean headers:", clean_headers)

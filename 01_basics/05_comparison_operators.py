"""
Phase 1 - Python Basics: Comparison Operators and Identity Checks
"""

a = 15
b = 20
c = 15

print("=== Comparison Expressions ===")
print(f"a == c: {a == c}")
print(f"a != b: {a != b}")
print(f"a < b:  {a < b}")
print(f"b >= c: {b >= c}")

# Chained comparisons (Pythonic syntax)
score = 85
is_passing_grade = 60 <= score <= 100
print(f"Is {score} within [60, 100]? {is_passing_grade}")

# Difference between equality (==) and identity (is)
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = list_1

print("
=== Equality (==) vs Identity (is) ===")
print(f"list_1 == list_2: {list_1 == list_2} (Same content)")
print(f"list_1 is list_2: {list_1 is list_2} (Different memory addresses)")
print(f"list_1 is list_3: {list_1 is list_3} (Exact same reference)")

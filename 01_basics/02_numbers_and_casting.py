"""
Phase 1 - Python Basics: Numeric Operations and Type Casting
"""

# Arithmetic Operators
a = 25
b = 4

print("=== Arithmetic Operations ===")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Standard Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulo (Remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Explicit Type Casting
raw_str_num = "100"
converted_int = int(raw_str_num)
converted_float = float(raw_str_num)
float_to_int = int(99.99)  # Truncates decimal, does not round

print("
=== Type Casting ===")
print(f"String to Int: {converted_int} ({type(converted_int)})")
print(f"String to Float: {converted_float} ({type(converted_float)})")
print(f"Truncated Float to Int (99.99): {float_to_int}")
print(f"Rounding: round(99.556, 2) = {round(99.556, 2)}")

# Boolean Casting Rules (Truthy vs Falsy)
print(f"bool(0) -> {bool(0)}")
print(f"bool(42) -> {bool(42)}")
print(f"bool('') -> {bool('')}")
print(f"bool('Python') -> {bool('Python')}")

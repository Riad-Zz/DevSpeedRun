"""
Phase 1 - Python Basics: Variables, Naming Conventions, and Primitive Types
"""

# Variable assignment and basic types
age: int = 22
gpa: float = 3.85
user_name: str = "Riad"
is_developer: bool = True
mystery_value = None

print("=== Variable Types and Values ===")
print(f"User: {user_name} ({type(user_name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"GPA: {gpa} ({type(gpa).__name__})")
print(f"Developer Status: {is_developer} ({type(is_developer).__name__})")
print(f"Empty/None: {mystery_value} ({type(mystery_value).__name__})")

# Multiple assignment & tuple unpacking
x, y, z = 10, 20, 30
print(f"Unpacked values: x={x}, y={y}, z={z}")

# Swapping variables without temporary variable
x, y = y, x
print(f"Swapped values: x={x}, y={y}")

# isinstance checking
assert isinstance(age, int)
assert isinstance(gpa, float)
assert isinstance(user_name, str)
print("[OK] Primitive type assertions passed.")

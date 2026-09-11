"""
Phase 1 - Loops: Nested Loops and Matrix Patterns
"""

# Multiplication Table 1 to 5
print("=== 5x5 Grid Table ===")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3d}", end=" ")
    print()

# Triangle Star Pattern
print("
=== Star Pyramid Pattern ===")
levels = 5
for i in range(1, levels + 1):
    spaces = " " * (levels - i)
    stars = "*" * (2 * i - 1)
    print(f"{spaces}{stars}")

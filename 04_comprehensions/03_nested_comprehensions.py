"""
Phase 1 - Comprehensions: Nested Comprehensions and Matrix Flattening
"""

# Generating a 3x3 identity matrix
identity_matrix = [[1 if r == c else 0 for c in range(3)] for r in range(3)]
print("Identity Matrix:")
for row in identity_matrix:
    print(row)

# Flattening a 2D matrix into a 1D list
grid = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
flattened = [val for row in grid for val in row]
print("Flattened Grid:", flattened)
assert flattened == [10, 20, 30, 40, 50, 60, 70, 80, 90]

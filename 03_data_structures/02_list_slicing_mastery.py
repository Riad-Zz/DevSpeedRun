"""
Phase 1 - Data Structures: Advanced List Slicing
"""

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print("Full list:", numbers)
print("First 3 [0:3]:", numbers[0:3])
print("From index 4 to end [4:]:", numbers[4:])
print("Every 2nd element [::2]:", numbers[::2])
print("Middle slice [2:7]:", numbers[2:7])
print("Reversed list [::-1]:", numbers[::-1])

# Shallow copy via slice
cloned_numbers = numbers[:]
cloned_numbers[0] = 999
assert numbers[0] == 0, "Original list should remain intact"
print("[OK] Slicing and cloning verified.")

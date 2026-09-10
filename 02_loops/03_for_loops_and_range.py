"""
Phase 1 - Loops: For Loops and Range Generator
"""

# Range variants: stop, start-stop, start-stop-step
print("=== Range Formats ===")
print("range(5):", list(range(5)))
print("range(2, 8):", list(range(2, 8)))
print("range(10, 50, 10):", list(range(10, 50, 10)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# Iterating over sequence
languages = ["Python", "JavaScript", "TypeScript", "Go", "Rust"]
print("
=== Iterating List ===")
for lang in languages:
    print(f"- Developer tool: {lang}")

# Accumulator loop
total_sum = 0
for num in range(1, 11):
    total_sum += num

print(f"
Sum from 1 to 10: {total_sum}")
assert total_sum == 55

"""
Phase 1 - Loops: Enumerate Index Tracking and Reversed Iteration
"""

milestones = ["Setup Environment", "Learn Syntax", "Build Projects", "Deploy Code"]

print("=== Enumerate with 1-based indexing ===")
for index, task in enumerate(milestones, start=1):
    print(f"Step {index:02d}: {task}")

# Reversed iteration
print("
=== Reversed Sequence ===")
for item in reversed(milestones):
    print(f"<- Backtracking: {item}")

# Step-skipping with slice in loop
even_indices = [task for idx, task in enumerate(milestones) if idx % 2 == 0]
print(f"
Even index tasks: {even_indices}")

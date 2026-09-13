"""
Phase 1 - Data Structures: In-place List Mutation
"""

tech_stack = ["Python", "Git"]

# Append single element
tech_stack.append("PostgreSQL")
print("After append:", tech_stack)

# Insert at specific index
tech_stack.insert(1, "Docker")
print("After insert at index 1:", tech_stack)

# Extend with another collection
cloud_tools = ["AWS", "Linux"]
tech_stack.extend(cloud_tools)
print("After extend:", tech_stack)

# Concatenation (+) vs Extend
combined = tech_stack + ["Redis"]
print("Concatenated (+):", combined)

"""
Phase 1 - Python Basics: String Operations, Methods, and Formatting
"""

message = "  learning Python SpeedRun is Amazing!  "

# Strip, Case conversion
clean_msg = message.strip()
print(f"Original: '{message}'")
print(f"Stripped: '{clean_msg}'")
print(f"Uppercase: {clean_msg.upper()}")
print(f"Lowercase: {clean_msg.lower()}")
print(f"Title Case: {clean_msg.title()}")

# Substring Search and Replacement
replaced = clean_msg.replace("Amazing", "Elite")
print(f"Replaced: {replaced}")
print(f"Starts with 'learning': {clean_msg.startswith('learning')}")
print(f"Count of 'i': {clean_msg.lower().count('i')}")

# Splitting and Joining
tokens = clean_msg.split()
rejoined = " -> ".join(tokens)
print(f"Tokens: {tokens}")
print(f"Rejoined: {rejoined}")

# Advanced F-string formatting
price = 149.5
quantity = 3
total = price * quantity
score_ratio = 7 / 9

print("
=== Formatted Output ===")
print(f"Product total: ${total:,.2f}")
print(f"Percentage: {score_ratio:.1%}")
print(f"Right-aligned: {'[OK]':>15}")

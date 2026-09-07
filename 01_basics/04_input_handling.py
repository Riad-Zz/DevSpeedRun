"""
Phase 1 - Python Basics: Input Handling and Safe Conversion
"""

def parse_user_age(raw_input: str) -> int:
    """Parses user input safely into an integer age."""
    clean = raw_input.strip()
    if not clean.isdigit():
        raise ValueError(f"'{raw_input}' is not a valid positive integer.")
    return int(clean)

def calculate_next_salary(current_salary: float, increment_pct: float) -> float:
    """Calculates updated salary based on percentage hike."""
    return current_salary * (1.0 + (increment_pct / 100.0))

# Demonstration without blocking interactive prompt
sample_age_str = " 25 "
sample_salary = 60000.0
sample_hike = 12.5

age = parse_user_age(sample_age_str)
projected_salary = calculate_next_salary(sample_salary, sample_hike)

print(f"Parsed Age: {age} years old")
print(f"Current Salary: ${sample_salary:,.2f}")
print(f"Next Year Projected: ${projected_salary:,.2f} (+{sample_hike}%)")

assert age == 25
assert round(projected_salary, 2) == 67500.0
print("[OK] Safe input handling validated.")

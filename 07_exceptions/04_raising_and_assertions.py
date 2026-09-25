"""
Phase 1 - Exceptions: Explicit Raising and Invariant Assertions
"""

def validate_age_for_registration(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"Expected int, got {type(age).__name__}")
    if age < 13:
        raise ValueError(f"Minimum age requirement is 13. Provided: {age}")
    print(f"Age {age} approved for registration.")

validate_age_for_registration(20)

# Exception chaining
def process_data(raw_val: str):
    try:
        return int(raw_val)
    except ValueError as err:
        raise RuntimeError("Data processing pipeline encountered bad input") from err

try:
    process_data("corrupt_input")
except RuntimeError as r_err:
    print(f"Caught chained exception: {r_err} (Original: {r_err.__cause__})")

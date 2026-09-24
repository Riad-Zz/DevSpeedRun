"""
Phase 1 - Exceptions: try and except Fundamentals
"""

def parse_integer(value_str: str) -> int | None:
    try:
        parsed = int(value_str)
        return parsed
    except ValueError as e:
        print(f"[WARN] Failed to parse integer: {e}")
        return None

print("Parsing '123':", parse_integer("123"))
print("Parsing 'abc':", parse_integer("abc"))
assert parse_integer("123") == 123
assert parse_integer("abc") is None

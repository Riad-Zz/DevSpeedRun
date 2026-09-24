"""
Phase 1 - Exceptions: Handling Multiple Exception Types and Hierarchy
"""

def execute_math_lookup(data: dict, key: str, divisor: int) -> float | str:
    try:
        number = data[key]
        return number / divisor
    except KeyError:
        return "Error: Specified key not found in data."
    except ZeroDivisionError:
        return "Error: Division by zero is not permitted."
    except TypeError:
        return "Error: Unsupported types for mathematical operation."

data_bank = {"base": 100, "text": "invalid"}

print(execute_math_lookup(data_bank, "base", 5))
print(execute_math_lookup(data_bank, "missing", 5))
print(execute_math_lookup(data_bank, "base", 0))
print(execute_math_lookup(data_bank, "text", 2))

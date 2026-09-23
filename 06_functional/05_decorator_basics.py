"""
Phase 1 - Functional Python: Decorator Fundamentals
"""

def simple_logger(func):
    """Decorator that logs execution entry and exit."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing '{func.__name__}' with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' completed. Result: {result}")
        return result
    return wrapper

@simple_logger
def greet_user(name: str, enthusiasm: int = 1) -> str:
    return f"Hello, {name}!" + ("!" * enthusiasm)

output = greet_user("Riad", enthusiasm=3)
print("Final output:", output)

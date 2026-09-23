"""
Phase 1 - Functional Python: Practical Decorators with functools.wraps
"""

import time
from functools import wraps

def benchmark_timer(func):
    """Decorator measuring execution time in milliseconds."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration_ms = (time.perf_counter() - start) * 1000
        print(f"[BENCHMARK] {func.__name__} took {duration_ms:.4f} ms")
        return result
    return wrapper

@benchmark_timer
def compute_sum_of_squares(limit: int) -> int:
    """Calculates sum of squares up to limit."""
    return sum(i * i for i in range(limit))

res = compute_sum_of_squares(50000)
print(f"Result computed: {res}")
print(f"Function name preserved: {compute_sum_of_squares.__name__}")
print(f"Doc preserved: {compute_sum_of_squares.__doc__}")

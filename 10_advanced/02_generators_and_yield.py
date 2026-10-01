"""
Phase 1 - Advanced: Generators and yield
"""

def fibonacci_generator(limit: int):
    """Generates Fibonacci numbers up to limit."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("First 10 Fibonacci numbers via generator:")
fib_series = list(fibonacci_generator(10))
print(fib_series)
assert fib_series == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

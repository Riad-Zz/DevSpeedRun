"""
Phase 1 - Functional Python: Closures and Function Factories
"""

def power_factory(exponent: int):
    """Returns a function that raises base to given exponent."""
    def power(base: int | float) -> int | float:
        return base ** exponent
    return power

square_func = power_factory(2)
cube_func = power_factory(3)

print("5 squared:", square_func(5))
print("3 cubed:", cube_func(3))
assert square_func(5) == 25
assert cube_func(3) == 27

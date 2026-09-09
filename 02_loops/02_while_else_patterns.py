"""
Phase 1 - Loops: While-Else Pattern and Prime Search
"""

def is_prime(number: int) -> bool:
    """Checks if a number is prime using while-else."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            # Found factor, not prime
            break
        divisor += 1
    else:
        # Loop finished naturally without a break
        return True
    return False

test_numbers = [2, 3, 4, 17, 25, 29, 31, 35]
results = {n: is_prime(n) for n in test_numbers}

print("=== Prime Search Results (while-else) ===")
for num, prime_status in results.items():
    print(f"{num:2d} is prime? {prime_status}")

assert results[29] is True
assert results[25] is False
print("[OK] While-else prime logic verified.")

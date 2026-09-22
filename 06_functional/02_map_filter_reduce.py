"""
Phase 1 - Functional Python: map(), filter(), and reduce()
"""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# map(): transforms each element
doubled = list(map(lambda x: x * 2, nums))
print("Doubled with map:", doubled)

# filter(): keeps elements where predicate is True
odds = list(filter(lambda x: x % 2 != 0, nums))
print("Odds with filter:", odds)

# reduce(): accumulates sequence into single value
product = reduce(lambda acc, val: acc * val, nums)
print("Product with reduce:", product)
assert product == 40320

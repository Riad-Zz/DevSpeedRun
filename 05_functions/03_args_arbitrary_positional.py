"""
Phase 1 - Functions: *args Positional Argument Packing and Unpacking
"""

def calculate_stats(*numbers: float) -> dict:
    """Calculates count, sum, average, min, and max of arbitrary numbers."""
    if not numbers:
        return {"count": 0, "total": 0, "avg": 0.0, "min": None, "max": None}
    
    total = sum(numbers)
    return {
        "count": len(numbers),
        "total": total,
        "avg": round(total / len(numbers), 2),
        "min": min(numbers),
        "max": max(numbers)
    }

print("Stats (10, 25, 40, 85):", calculate_stats(10, 25, 40, 85))

# Unpacking a list into *args
test_vals = [5, 15, 25, 35, 45]
unpacked_stats = calculate_stats(*test_vals)
print("Stats from unpacked list:", unpacked_stats)
assert unpacked_stats["total"] == 125

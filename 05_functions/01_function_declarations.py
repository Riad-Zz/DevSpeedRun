"""
Phase 1 - Functions: Definitions, Parameters, and Return Signatures
"""

def compute_circle_metrics(radius: float) -> tuple[float, float]:
    """Calculates circumference and area for a given radius."""
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return round(circumference, 2), round(area, 2)

circ, area = compute_circle_metrics(5.0)
print(f"Radius 5.0 -> Circumference: {circ}, Area: {area}")

# Function docstring inspection
print(f"Docstring: {compute_circle_metrics.__doc__.strip()}")

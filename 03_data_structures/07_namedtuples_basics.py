"""
Phase 1 - Data Structures: namedtuple for Self-Documenting Data
"""

from collections import namedtuple

# Tuples as hashable dictionary keys
location_cache = {
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("Location at (40.7128, -74.0060):", location_cache[(40.7128, -74.0060)])

# namedtuple class factory
Student = namedtuple("Student", ["name", "roll_no", "grade"])
student_1 = Student(name="Kamal", roll_no=101, grade="A+")

print(f"Student: {student_1.name}, Roll: {student_1.roll_no}, Grade: {student_1.grade}")
print(f"Indexed access: {student_1[0]}")
assert student_1.grade == "A+"

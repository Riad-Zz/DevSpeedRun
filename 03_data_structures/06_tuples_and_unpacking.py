"""
Phase 1 - Data Structures: Tuples and Immutability
"""

# Tuples are immutable ordered sequences
coordinates = (37.7749, -122.4194)
single_tuple = (42,)  # Comma is required for single-element tuple

print(f"Coordinates tuple: {coordinates}")
print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")

# Tuple Unpacking
lat, lon = coordinates
print(f"Unpacked: lat={lat}, lon={lon}")

# Extended unpacking with *rest
data_stream = (100, 200, 300, 400, 500, 600)
first, *middle, last = data_stream
print(f"First: {first}")
print(f"Middle values: {middle}")
print(f"Last: {last}")

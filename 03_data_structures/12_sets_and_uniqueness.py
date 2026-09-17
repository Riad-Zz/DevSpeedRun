"""
Phase 1 - Data Structures: Sets, Deduplication and Membership Testing
"""

# Deduplication
raw_tags = ["python", "ai", "web", "python", "backend", "ai", "fastapi"]
unique_tags = set(raw_tags)
print("Raw tags list:", raw_tags)
print("Deduplicated set:", unique_tags)

# Set Mutability
unique_tags.add("docker")
unique_tags.discard("nonexistent")  # Safe, no KeyError
print("After adding 'docker':", unique_tags)

# Fast O(1) membership lookup
is_fastapi_present = "fastapi" in unique_tags
print(f"Is 'fastapi' in tags? {is_fastapi_present}")
assert is_fastapi_present is True

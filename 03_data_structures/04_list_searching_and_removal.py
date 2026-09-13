"""
Phase 1 - Data Structures: Searching and Removing Elements from Lists
"""

queue = ["Auth Service", "Billing Service", "Notification Service", "Auth Service"]

# Search
first_auth_idx = queue.index("Auth Service")
auth_count = queue.count("Auth Service")
print(f"First 'Auth Service' index: {first_auth_idx}, Count: {auth_count}")

# Remove by value (removes first occurrence)
queue.remove("Auth Service")
print("After remove('Auth Service'):", queue)

# Pop by index (returns popped item)
popped_service = queue.pop(0)
print(f"Popped index 0: {popped_service}, Remaining: {queue}")

# Pop last (LIFO stack behavior)
last_service = queue.pop()
print(f"Popped last: {last_service}, Remaining: {queue}")

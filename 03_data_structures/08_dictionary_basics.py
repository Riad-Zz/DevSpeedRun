"""
Phase 1 - Data Structures: Dictionaries and Key Hashing
"""

# Creating dictionaries
user_profile = {
    "username": "riad_dev",
    "email": "riad@example.com",
    "reputation": 1420,
    "is_active": True
}

print("Profile:", user_profile)
print("Username:", user_profile["username"])

# Safe access with .get() avoids KeyError
missing_role = user_profile.get("role", "Standard Member")
print("Role (fallback default):", missing_role)

# Adding and updating keys
user_profile["reputation"] += 50
user_profile["location"] = "Dhaka"
print("Updated profile:", user_profile)

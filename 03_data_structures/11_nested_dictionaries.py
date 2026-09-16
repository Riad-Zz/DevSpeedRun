"""
Phase 1 - Data Structures: Nested Dictionaries and Safe Deep Retrieval
"""

organization = {
    "engineering": {
        "lead": "Riad",
        "team_size": 15,
        "stacks": ["Python", "FastAPI", "React"]
    },
    "design": {
        "lead": "Amina",
        "team_size": 6,
        "tools": ["Figma", "Blender"]
    }
}

print("Engineering Lead:", organization["engineering"]["lead"])
print("Engineering Primary Stack:", organization["engineering"]["stacks"][0])

# Safe nested lookup function
def safe_deep_get(dictionary: dict, *keys, default=None):
    curr = dictionary
    for k in keys:
        if isinstance(curr, dict):
            curr = curr.get(k)
            if curr is None:
                return default
        else:
            return default
    return curr

lead_name = safe_deep_get(organization, "engineering", "lead")
missing_val = safe_deep_get(organization, "marketing", "budget", default=0)
print(f"Safely retrieved lead: {lead_name}")
print(f"Safely retrieved missing budget: {missing_val}")

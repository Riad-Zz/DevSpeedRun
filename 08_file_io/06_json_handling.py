"""
Phase 1 - File I/O: JSON Serialization and Deserialization
"""

import json

developer_data = {
    "name": "Riad",
    "journey": "DevSpeedRun",
    "level": "Phase 1 - Python Mastery",
    "completed_topics": ["Types", "Loops", "Functions", "OOP", "I/O"],
    "metrics": {
        "commits": 70,
        "active_days": 27
    }
}

# Serialize to JSON string
json_str = json.dumps(developer_data, indent=2)
print("Serialized JSON:\n" + json_str)

# Deserialize back to Python dict
parsed = json.loads(json_str)
print("\nDeserialized Developer Name:", parsed["name"])
assert parsed["metrics"]["commits"] == 70

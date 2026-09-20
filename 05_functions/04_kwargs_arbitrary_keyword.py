"""
Phase 1 - Functions: **kwargs Keyword Argument Packing
"""

def generate_dev_profile(username: str, **attributes) -> None:
    """Prints a developer profile formatted from arbitrary keyword arguments."""
    print(f"Developer Profile: @{username}")
    for key, value in attributes.items():
        formatted_key = key.replace("_", " ").title()
        print(f"  - {formatted_key}: {value}")

generate_dev_profile(
    "riad_speedrun",
    primary_language="Python",
    experience_years=3,
    framework="FastAPI",
    speciality="Backend Architecture"
)

# Unpacking dictionary into **kwargs
config = {"timeout": 30, "retries": 3, "verbose": True}
def configure_client(**options):
    print("Configured client with options:", options)

configure_client(**config)

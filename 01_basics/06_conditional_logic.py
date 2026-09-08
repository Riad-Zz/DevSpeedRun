"""
Phase 1 - Python Basics: Conditional Branching and Ternary Syntax
"""

def evaluate_match_status(goals: int, time_left: int, is_home_game: bool) -> str:
    """Evaluates game situation based on conditional statements."""
    if goals >= 3 and time_left > 10:
        return "Dominating performance! Victory is assured."
    elif goals >= 1 and is_home_game:
        return "Solid home advantage, fighting hard."
    elif goals == 0 and time_left < 15:
        return "High urgency, need an equalizer immediately!"
    else:
        return "Standard competitive match in progress."

print(evaluate_match_status(3, 25, True))
print(evaluate_match_status(1, 40, True))
print(evaluate_match_status(0, 5, False))

# Python Ternary (Conditional Expression)
level = 80
status = "Veteran" if level >= 50 else "Novice"
print(f"Player level {level} status: {status}")

# Short-circuit evaluation
default_name = ""
display_name = default_name or "Anonymous Player"
print(f"Display name: {display_name}")

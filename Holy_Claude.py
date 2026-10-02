# ==============================================================================
# DevSpeedRun - Master Python Learning Journey (Holy_Claude)
# Complete Phase 1: Python Fundamentals, Data Structures, OOP & Advanced
# ==============================================================================

print("Holy claude , What the hell ! Welcome to DevSpeedRun Master Track!")

# 1. Variable and Data Types
age = 22
name = "Riad"
sentence = f"{name} is {age} years old and speedrunning Python!"
print(sentence, f"Type: {type(sentence).__name__}")

# 2. Safe Input, Output, and Conversion
salary = 75000
increment = 15.0
projected_salary = salary + (salary * (increment / 100.0))
print(f"{name}, your projected salary next year will be: ${projected_salary:,.2f}")

# 3. Conditional and Logic Gates
goal = 3
time_left = 15
is_home_game = True

if goal >= 3 and time_left <= 20:
    print("Match Status: Victory locked in!")
elif goal < 3 and is_home_game:
    print("Match Status: Home support pushing for a comeback!")
else:
    print("Match Status: Great competitive game.")

# 4. Loops (While and For with Enumerate & Range)
while goal < 7:
    goal += 1
    if goal == 7:
        print(f"Goal {goal}: Suiiiiiii!")
        break

languages = ["Python", "JavaScript", "TypeScript", "Go", "Docker"]
for index, lang in enumerate(languages, start=1):
    print(f"Tech Skill {index:02d}: {lang}")

# 5. Functions & Type Annotations
def calculate_metrics(base: float, multiplier: float = 1.5) -> float:
    """Calculates scaled metric score."""
    return base * multiplier

print(f"Metric Score: {calculate_metrics(40.0)}")

# 6. Lists, Slicing and Methods
players = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland"]
print("Top 3 players:", players[:3])
print("Reversed squad:", players[::-1])
players.append("Vinicius")
removed = players.pop(1)
players.sort()
print(f"Removed {removed}. Alphabetical roster: {players}")

# 7. Dictionaries and Sets
dev_profile = {
    "username": "riad_dev",
    "track": "SpeedRun",
    "phase": 1,
    "completed": True
}
for key, value in dev_profile.items():
    print(f"  {key.capitalize()} -> {value}")

unique_frameworks = {"FastAPI", "Django", "FastAPI", "Flask"}
unique_frameworks.add("FastAPI")
print("Unique Frameworks Set:", unique_frameworks)

# 8. List & Dict Comprehensions
numbers = list(range(1, 11))
even_squares = [n**2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)
square_mapping = {n: n**2 for n in numbers[:5]}
print("Square mapping dict:", square_mapping)

# 9. *args, **kwargs and Lambda Functions
def aggregate_points(*scores):
    return sum(scores)

def user_config(username, **settings):
    print(f"Configuring @{username}:", settings)

print("Aggregated scores (*args):", aggregate_points(10, 20, 30, 40))
user_config("Riad", role="Admin", speedrun=True, level="Phase1-Master")

multiply = lambda x, y: x * y
print("Lambda multiply(7, 8):", multiply(7, 8))

# 10. Robust Exception Handling (try, except, else, finally)
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Only numbers allowed!"
    else:
        return f"Result is {result}"
    finally:
        print("[Log] safe_divide executed cleanly.")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 11. Reference to Organized Phase 1 Modules
print("\n[SUCCESS] Phase 1 Curriculum Complete! Explore subdirectories: 01_basics to 11_mini_projects.")

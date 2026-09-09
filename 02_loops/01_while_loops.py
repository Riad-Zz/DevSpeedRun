"""
Phase 1 - Loops: While Loop Fundamentals, Break, and Continue
"""

print("=== Basic While Counter ===")
count = 1
while count <= 5:
    print(f"Step {count}")
    count += 1

print("
=== Break and Continue in While Loop ===")
val = 0
while val < 10:
    val += 1
    if val == 4:
        print(f"Skipping {val} (continue)")
        continue
    if val == 8:
        print(f"Hit limit at {val}! Halting loop (break)")
        break
    print(f"Processed value: {val}")

# Countdown with Sentinel
timer = 3
while timer > 0:
    print(f"Liftoff in {timer}...")
    timer -= 1
print("🚀 Blastoff!")

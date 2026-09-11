"""
Phase 1 - Loops: Parallel Iteration with zip()
"""

players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
clubs = ["Inter Miami", "Al Nassr", "Al Hilal", "Real Madrid"]
jerseys = [10, 7, 10, 9]

print("=== Parallel Traversal with zip ===")
for player, club, number in zip(players, clubs, jerseys):
    print(f"#{number:2d} | {player:<10} -> {club}")

# Building a dictionary from paired sequences
player_roster = dict(zip(players, clubs))
print("
Constructed Dictionary:", player_roster)
assert player_roster["Messi"] == "Inter Miami"

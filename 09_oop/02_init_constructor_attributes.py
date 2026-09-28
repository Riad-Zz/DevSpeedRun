"""
Phase 1 - OOP: The __init__ Constructor Method
"""

class Player:
    def __init__(self, username: str, role: str, rating: int = 1200):
        self.username = username
        self.role = role
        self.rating = rating
        self.inventory = []

    def add_item(self, item: str) -> None:
        self.inventory.append(item)
        print(f"Added {item} to {self.username}'s inventory.")

p1 = Player("SpeedRunner", "Warrior", 1450)
p1.add_item("Golden Keyboard")
print(f"Player: {p1.username} | Role: {p1.role} | Rating: {p1.rating}")
print(f"Inventory: {p1.inventory}")

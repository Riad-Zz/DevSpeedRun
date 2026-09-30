"""
Phase 1 - OOP: Class Inheritance and Method Overriding
"""

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def attack(self) -> str:
        return f"{self.name} attacks with basic punch."

class Mage(Character):
    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.mana = mana

    def attack(self) -> str:
        # Overridden method
        return f"{self.name} casts Fireball! (Mana left: {self.mana - 10})"

mage = Mage("Gandalf", 100, 50)
print(mage.attack())
assert isinstance(mage, Character)

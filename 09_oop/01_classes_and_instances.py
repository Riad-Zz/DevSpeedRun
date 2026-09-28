"""
Phase 1 - OOP: Classes, Instances, and Methods
"""

class Developer:
    """Represents a software developer in DevSpeedRun."""
    
    def introduce(self, name: str, specialty: str) -> None:
        print(f"Hello, I am {name}, specializing in {specialty}.")

dev = Developer()
dev.introduce("Riad", "Backend Systems")

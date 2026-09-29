"""
Phase 1 - OOP: Pythonic Getters and Setters with @property
"""

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

t = Temperature(25.0)
print(f"Celsius: {t.celsius}°C")
print(f"Fahrenheit: {t.fahrenheit}°F")

t.celsius = 30.0
print(f"Updated Fahrenheit: {t.fahrenheit}°F")

"""
Phase 1 - OOP: super() Delegating Methods and Multi-level Hierarchy
"""

class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def get_specs(self) -> str:
        return f"{self.brand} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str, battery_kwh: int):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

    def get_specs(self) -> str:
        base_specs = super().get_specs()
        return f"{base_specs} [{self.battery_kwh} kWh Battery]"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.get_specs())

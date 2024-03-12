class Vehicle:

    def __init__(self, brand, model, fuel_tank_capacity, fuel_consumption):
        self.brand = brand
        self.model = model
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_efficiency(self):
        return self.fuel_tank_capacity / self.fuel_consumption


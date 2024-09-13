class Car:
    def __init__(self, brand, model):
        self.__brand  = brand
        self.model = model
    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return f"{super().full_name()} with {self.battery_size} of battery"
    
tesla = ElectricCar("Tesla", "Model S", "100kWh")
print(tesla.full_name())
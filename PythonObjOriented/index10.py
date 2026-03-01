#Composition = composed object directly owns its components which can't exist independently
#              "Owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

    def __str__(self):
        return f"{self.horse_power} hp"

class Wheel:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size} inch"

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def display_car(self):
        wheels_str = ", ".join(str(wheel) for wheel in self.wheels)
        return f"{self.make} {self.model} | Engine: {self.engine} | Wheels: {wheels_str}"

car = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)

print(car.display_car())

# Object = A 'Bundle' of related attribute and method function
# Ex Phone, cup, book
# You need a 'class' to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("cortte", 2025, "black", True)
car3 = Car("charger", 2022, "white", True)

# print(car1.model)
# print(car1.year)
# print(car3.color)
# print(car3.for_sale)


car2.drive()
car3.stop()

# Static Methods = A method that belongs to a class rather than any object from the class (inheritance)
#                  usually used for general utility functions

# Instance Methods = Best for operation on instances of the class (objects)
# Static Method = Best for utility that does not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} : {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Rocket Scientist"))

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongbob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

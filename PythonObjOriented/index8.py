#DUCK Typing =  Another way to achieve polymorphism beside inheritence
#               object must have  the minimum necessary attribute/methods
#                "If it looks  like a duck and quack like a duck , it must be duck"

class Animal:
    alive = True



class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:
    def speak(self):
        print("HONK!")


animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
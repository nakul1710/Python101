#Abstract Class in Python
#An abstract class is a class that cannot be instantiated and is used as a blueprint for other classes.
#It contains abstract methods (methods without implementation) that must be implemented by child classes.
#Why Use Abstract Classes?
#To enforce a common interface
#To ensure subclasses implement required methods


from abc import ABC, abstractmethod


class vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass 

class Car(vehicle):

    def go(self):
        print("You drive the Car")

    def stop(self):
        print("You stop the Car")

car = Car()
car.go()
car.stop()

class Motercycle(vehicle):

    def go(self):
        print("You drive the Car")

    def stop(self):
        print("You stop the Car")

motercycle = Motercycle()
motercycle.go()
motercycle.stop()
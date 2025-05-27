# abstraction
# a class that contains one or more methods
# Abstract class and interfaces
from abc import ABC, abstractmethod  # Abstraction


class Vehicle(ABC):
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        print("Car engine started")


class Bike(Vehicle):
    def start(self):
        print("Bike engine started")


# NOTES
# We cannot create objects of abstract classes
# vehicle = Vehicle()  # This will raise an error
car = Car()
bike = Bike()
# Call the start method
car.start()  # Output: Car engine started
bike.start()  # Output: Bike engine started
# Call the start method on the abstract class
Vehicle().start()  # Output: Vehicle started
# EXERCISE
# Submit your work on github for method overriding and method resolution order(MRO)
# Uni system
# University System to display information of Student,Parent and lecturer

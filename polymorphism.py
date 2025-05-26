# Polymorphism
# What is polymorphism?
# Example:Polymorphism with inheritance
# Superclass
class Bird:
    def fly(self):
        print("Birds fly in the sky")


# derived class
class Eagle(Bird):
    def fly(self):
        print("Eagles fly at high altitudes")


class Sparrow(Bird):
    def fly(self):
        print("Sparrows fly at low altitudes")


# How we use polymorphism
def flight_test(bird):
    bird.fly()


# Create object
eagle = Eagle()
sparrow = Sparrow()
# Call the flight_test method with different
flight_test(eagle)  # Output: Eagles fly at high altitudes
flight_test(sparrow)  # Output: Sparrows fly at low altitudes
flight_test(Bird())  # Output: Birds fly in the sky

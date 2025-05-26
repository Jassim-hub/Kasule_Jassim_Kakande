# Key principles in oop
# 1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class).
# 2. Abstraction: Hiding complex implementation details and showing only the essential features of the object.
# 3. Inheritance: Mechanism to create a new class using properties and methods of an existing class.
# 4. Polymorphism: Ability to present the same interface for different data types or classes.
# 5.Method Overriding: Redefining a method in a derived class that already exists in the base class.
# 6. Method Overloading: Creating multiple methods with the same name but different parameters in the same class.
# class Animal:
#     def speak(self):
#         print("Some generic animal sound")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
# cat = Cat()
# cat.speak()
# cat.sound()
class Father:
    def skill(self):
        print("Father's skill: Carpentry")


class Mother:
    def skill(self):
        print("Mother's skill: Cooking")


class Child(Father, Mother):
    def skills(self):
        print("Child's skills:")
        Father.skill(self)
        Mother.skill(self)


# Create an instance of Child and call the skills method
child = Child()
child.skills()
# Output:
# Child's skills:
# Father's skill: Carpentry
# Mother's skill: Cooking

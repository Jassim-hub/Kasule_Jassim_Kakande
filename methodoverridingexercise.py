# Method overriding exercise
# Method Overriding Exercise
class Person:
    def display_info(self):
        print("This is a person.")


class Student(Person):
    def display_info(self):
        print("This is a student.")


class Parent(Person):
    def display_info(self):
        print("This is a parent.")


class Lecturer(Person):
    def display_info(self):
        print("This is a lecturer.")


# Create instances of each class
student = Student()
parent = Parent()
lecturer = Lecturer()
person = Person()
# Call the display_info method for each instance
student.display_info()
parent.display_info()
lecturer.display_info()
person.display_info()

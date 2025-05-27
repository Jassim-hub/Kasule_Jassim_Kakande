class University:
    def display_info(self):
        print("University Information")


class Student(University):
    def display_info(self):
        name = input("Enter Student Name: ")
        reg_No = input("Enter Registration Number: ")
        self.name = name
        self.reg_No = reg_No
        print(f"Student Name: {self.name}, Registration Number: {self.reg_No}")


class Parent(University):
    def display_info(self):
        name = input("Enter Parent Name: ")
        relation = input("Enter Relation to Student: ")
        self.name = name
        self.relation = relation
        print(f"Parent Name: {self.name}, Relation: {self.relation}")


class Lecturer(University):
    def display_info(self):
        name = input("Enter Lecturer Name: ")
        subject = input("Enter CourseUnit Taught: ")
        self.name = name
        self.subject = subject
        print(f"Lecturer Name: {self.name}, CourseUnit: {self.subject}")


student = Student()
parent = Parent()
lecturer = Lecturer()

student.display_info()
parent.display_info()
lecturer.display_info()

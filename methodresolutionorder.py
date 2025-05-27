# Method Resolution Order (MRO) Exercise
class A:
    def method(self):
        print("Method from class A")


class B(A):
    def method(self):
        print("Method from class B")


class C(A):
    def method(self):
        print("Method from class C")


class D(B, C):
    def method(self):
        print("Method from class D")


# Create an instance of class D
d_instance = D()
# Call the method
d_instance.method()
# Check the Method Resolution Order (MRO)
print(D.__mro__)

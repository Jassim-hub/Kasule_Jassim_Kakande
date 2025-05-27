# def square(x):
#     return x * x
# print(square(5))
mylist = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, mylist))
print(squared)


# Find the factorial of a number using lambda function
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(5))

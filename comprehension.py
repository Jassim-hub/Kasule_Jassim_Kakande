"""""
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)
""" ""

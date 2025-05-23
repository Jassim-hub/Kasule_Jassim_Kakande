# 1:Syntax errors
# 2:Runtime errors
# 3:Logical errors

# Block of codes try, except, else, finally

# Example try to divide 5/0(zero division error)
# try:
#     result = 5 / 2
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# else:
#     print("Division successful, result is:", result)
# finally:
#     print("Execution completed.")
# Exercise
# Raise a custom exception that checks for a positive number
try:
    number = int(input("Enter an even number: "))
    if number % 2 == 0:
        raise ValueError("The number even.")
except ValueError as e:
    print("Error:", e)
else:
    print("The number is not even.")
finally:
    print("Execution completed.")
# Assignment two:
# Write a program to handle errors, the program should ask for 2 numbers using input and then divides tem. Use an infinite loop to keep asking until the valid input is provided.

import random

random_number = random.randint(1, 10)
guess = int(input("Guess the number its between 1 and 10:"))
while guess != random_number:
    print("Wrong guess, try again")
    if guess == random_number:
        print("You guessed it right")
        break
    else:
        guess = int(input("Guess the number its between 1 and 10:"))
print("You guessed it right")
print("The number was", random_number)

# import random
# guess = int(input("Guess the secret number between 1 and 10: "))

# secret_number = random.randint(1, 11)

# if guess == secret_number:
#     print(f"Congratulations! You guessed the secret number. The secret number is {secret_number}")
# else:
#     print(f"Sorry, that's not the secret number. The secret number is {secret_number}. Try again!")

# Ask the user for a number and print whether it is even or odd.
# number = int(input("Enter any number here: "))

# +, -, *, /, //

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"Number is not even")


# Ask the user for their age.

# If they are 18 or older, print "Adult".
# Otherwise print "Minor".

# age = int(input("Enter your age here: "))

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# Exercise 3 – Positive, Negative or Zero

# Ask the user to enter a number.

# Determine whether it is:

# Positive
# Negative
# Zero

# number = int(input("Enter your number here: "))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Neutral")

# number = "password123"

# password = input("Enter your password here: ")

# if password.lower() == number:
#     print("Access Granted")
# else:
#     print("Access Denied")

# Exercise 5 – Largest Number

# Ask the user for two numbers.

# Print which one is larger.

# If they are equal, print that they are equal.

number1 = int(input("Enter your first number here: "))
number2 = int(input("Enter your second number here: "))

if number1 > number2:
    print(f"{number1} is larger")
elif number1 < number2:
    print(f"{number2} is larger")
else:
    print(f"{number2} is equals to {number1}")
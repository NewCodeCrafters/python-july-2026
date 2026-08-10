# Use a while loop to print the numbers from 1 to 10.

# number = 1

# while number <= 10:
#     print(number)
#     number += 1


# Write a program that counts down from 10 to 1, then prints "Blast off!".

# number = 10
# while number >= 1:
#     print(number)
#     number -= 1
# else:
#     print("Blast off!")

# Ask the user to enter a number. Keep asking them to enter a number until they enter 0.

while True:
    number = int(input("Enter your number here: "))
    if number == 0:
        break
    else:
        continue
# else:
#     print("Hello")

# Create a program that repeatedly asks the user for a password until they enter the correct password.
correct_password = "O3916"

while True:
    password = input("enter your password here: ")
    if password == correct_password:
        break
    else:
        continue

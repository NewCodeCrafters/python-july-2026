
# # 23. **Print Even Numbers**
# #     Use a `while` loop to print all even numbers from **2 to 20**.

# number = 2
# while number <= 20:
#     print(number)
#     number += 2

# # 24. **Print Odd Numbers**
# #     Use a `while` loop to print all odd numbers from **1 to 19**.
# number = 1
# while number <= 20:
#     print(number)
#     number += 2

# # 25. **Multiplication Table**
# #     Ask the user for a number and use a `while` loop to print its multiplication table from **1 to 12**.
# number = int(input("Enter any number here: "))
# initial = 1
# while initial <= 20:
#     print(f"{number} * {initial} = {number * initial}")
#     initial += 1

# # 26. **Count Up by 2**
# #     Use a `while` loop to print:

# # ```text
# # 2
# # 4
# # 6
# # 8
# # 10
# # 12
# # 14
# # 16
# # 18
# # 20
# # ```

# temp = 2

# while temp <= 20:
#     print(temp)
#     temp += 2


# # 27. **Keep Asking for a Name**
# #     Ask the user to enter their name. Continue asking until they enter **"exit"**.

# while True:
#     name = input("Enter your name here to continue or exit to stop. ")
#     if name.lower() == "exit":
#         break
#     else:
#         continue

# # 28. **Number Range**
# #     Ask the user for a starting number and an ending number. Use a `while` loop to print every number between them.
# start = int(input("Enter your start number here: "))
# end = int(input("Enter your end number here: "))

# while start <= end:
#     print(start)
#     start += 1

# # 29. **Positive Number Checker**
# #     Keep asking the user to enter a number until they enter a **positive number**.
# while True:
#     number = int(input("Enter your number here: "))
#     if number > 0:
#         break
# # 30. **Limited Attempts**
# #     Ask the user to enter a password. Give them **3 attempts** to enter the correct password. After 3 incorrect attempts, display a message saying they have run out of attempts.

# secret = "Bulaba"
# attempts = 3
# while True:
#     password = input("Enter your password here: ")
#     if password == secret:
#         print("You got it right")
#         break
#     elif password != secret and attempts > 0:
#         print("Incorrect password")
#         attempts -= 1
#     else:
#         print("You've run out of options")
#         

# define function and call function
# def praise_myself():
#     print("I love myself")

# praise_myself()

# def greet_people(fname, lname, oname="Olowo"):
#     print(f"Welcome {fname} {lname} {oname}")

# name1 = input("Enter your first name here: ")
# name2 = input("Enter your last name here: ")
# name3 = input("Enter your other name: ")

# # positional Argument
# greet_people(name1, name2, name3)

# # Key word argument
# greet_people(oname=name3, fname=name1, lname=name2)

# Create a function larger_number(a, b) that prints the larger number.
# def larger_number(num1, num2):
#     """_summary_ I love myself

#     Args:
#         num1 (_type_): _description_
#         num2 (_type_): _description_
#     """

#     if num1 > num2:
#         print(num1)
#     elif num1 < num2:
#         print(num2)
#     else:
#         print("Both numbers are equal")

# larger_number(12, 13)

def calculator(a, b, operation):

    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print(a/b)
    else:
        print("Invalid Operation")

num1 = int(input("Enter your number here: "))
num2 = int(input("Enter your number here: "))
operation = input("Enter your operation here (+ - * or /): ")

calculator(num1, num2, operation)


#Write a function that prints your full name on the line

def my_name(first_name, last_name, full_name):

    first_name = str(input("Enter your firstname:"))
    last_name = str(input("Enter your lastname:"))
    full_name = (f"{first_name} {last_name}")

    print(f"my name is {full_name} ")

my_name("first_name", "last_name", "full_name")

#Write a function that receives one number and prints the multiplication table for that number from 1 to 10


def table():
    number = int(input("Enter your number:"))
    initial_number = 1
    while initial_number <= 10:
        print(f"{number} * {initial_number} = {number * initial_number}")
        initial_number += 1

table()  








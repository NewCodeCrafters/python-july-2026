from operations import *

def get_operations(num1:int, num2:int, operator:str):
    if operator == "+":
        total = add_two_numbers(num1, num2)
        with open("/Users/user/dev/python-july-2026/calculator/history.txt", "a") as file:
            file.write(f"{num1} + {num2} = {total}")

from math import pow, factorial

from random import randint, choices, choice
import string

print(pow(5, 2))
secret_number = randint(1, 10)

print(secret_number)
# factorial

names = ["Ore", "Maleek", "Uthman", "Muhammed", "Emmanuel", "Destiny", "John"]

random_name = choices(names, k=3)

print(random_name)

def get_factorial(num):
    """This function gets the factorial total of a number

    Args:
        num (int): Enter any number you want to get the factorial

    Returns:
        float: factorial total returned as float
    """
    total = 1
    for i in range(1, num+1):
        total *= i

    return total


# num = get_factorial()

from datetime import datetime

today = datetime.now()

# Format the date
# %A = Full weekday name
# %d = Day of the month as a zero-padded number
# %B = Full month name
# %Y = Four-digit year
formatted_date = today.strftime("%A, %d %B %Y")
print(formatted_date)
# Print today's date formatted as "Tuesday, 01 September 2026".
# Ask the user to enter a year.
# Determine whether it is a leap year

year = int(input("Enter a year here: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}is a leap year")
else:
    print(f"if {year} is not a leap year")

## Exercise 13 – Dice Roll

# Generate a random number from **1 to 6**.

# Ask the user for a guess.

# Print:

# * Correct
# * Incorrect

import random
guess =int(input("Guess the random number from 1 to 6: "))
random_number = random.randint(1,7)
if guess ==random_number:
    print("correct")
else:
    print("print incorrect")

## Exercise 18 – Rock, Paper, Scissors

#  The computer randomly chooses:

# * Rock
# * Paper
# * Scissors

# Ask the user to choose one.

# Determine whether the user:
# * Wins
# * Loses
# * Draws

import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Choose rock, paper, or scissors: ")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

## Exercise 23 – ATM Withdrawal

# Ask the user for:
# * Account balance
# * Withdrawal amount

# Determine whether the withdrawal can be completed.

account_balance = float(input("Enter your account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
if withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. New balance: {account_balance}")
else:
    print("Insufficient funds for this withdrawal.")

## Exercise 28 – Weekend Checker

# Ask the user to enter a days of the week

# Print wether it is :
#  *  Weekend
#  *  Weekday
 

day = input("Enter a day of the week: ")
if day.lower() in ["saturday", "sunday"]:
    print(f"{day} is a weekend.")
else:
    print(f"{day} is a weekday.")
    




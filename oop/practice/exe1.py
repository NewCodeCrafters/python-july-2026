# 1. Bank Account System

# Classes: Account, Transaction, Customer

# Tests: private balance with deposit/withdraw methods, validation, transaction history

# Watch for: Are they exposing fields directly? Do they validate in setters, or only in the UI?
from typing import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class Account:
    
    def __init__(self, account_number):
        self.account_number = account_number
        self._balance = 0

    def deposit(self, amount:float):
        if amount > 0:
            self._balance += amount
            return f"{amount} deposited successfully"
        else:
            return "Deposit must be greater than 0"

    def withdrawal(self, amount):
        if amount < 0:
            return "Withdrawn amount must be greater than 0"
        
        if amount > self._balance:
            return "Insufficient Funds"

        self._balance -= amount
        return f"{amount} withdrawn successfully"



class Transaction:
    def __init__(self, types:TransactionType, amount, timestamp):
        self.types = types
        self.amount = amount
        self.timestamp = timestamp



class Customer:
    bank = "UBA"
    
    def __init__(self, user_id, first_name, last_name, phone_number):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_info(self):
        return f"Full name is {self.first_name} {self.last_name}. Phone number is {self.phone_number}"


# 2. Library Management

# Classes: Book, Member, Loan, Library

# Tests: borrowing rules, due dates, availability tracking

# Watch for: Is Library a god class? Do Book and Member actually hold their own state?

# 3. Shape Calculator

# Classes: Shape (abstract), Circle, Rectangle, Triangle

# Tests: area/perimeter polymorphism

# Watch for: Do they use inheritance properly, or just if/else on a type string?
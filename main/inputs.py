# name = 'Muhammed'

# print(name[0:3])

# Registration Form with python

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone_number = input("Enter your phone number: ")
# age = input("Enter your age here: ")
yob = int(input("Enter your year of birth: "))

age = 2026 - yob

sentence = f"Welcome to Python Social network. Thanks for providing your information. Your full name is {first_name.title()} {last_name.title()}. Your phone number is {phone_number} and you are {age} years old."
print(sentence)
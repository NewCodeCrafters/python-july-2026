# 1. Write a function that receives a temperature in Celsius and returns the equivalent temperature in Fahrenheit.
# (20°C × 9/5) + 32 = 68°F

# def celcius_to_farenheit(temp:float):
#     conversion = (temp * 9/5) + 32
#     print(f"{temp} degree celcius is {conversion} degrees farenheit")

# celcius_to_farenheit(90)

# C = (°F − 32) × 5/9

def farenheit_to_celcius(temp:float):
    conversion = (temp - 32) * 5/9
    print(f"{temp} degree farenheit is {conversion} degrees celcius")

# Convert from celcius to kelvin

# 5. Write a function that receives a list of numbers and returns the smallest number in the list.

# [1, 2, 3, 21]
# def get_smallest_number(numbers:list):
#     smallest = numbers[0]
#     for i in numbers:
#         if i < smallest:
#             smallest = i
#         else:
#             continue
#     print(smallest)

# get_smallest_number([92, 12, 48, 14, 2, 15])



# def get_smallest_number(numbers:list):
#     print(min(numbers))

# get_smallest_number([92, 12, 48, 14, 2, 15, 0, -14])


# 5. Write a function that receives a year and returns whether it is a leap year.
# Step 1: Check if the year is divisible by 4 (Year ÷ 4 leaves a remainder of 0). If no, it is a normal year. If yes, move to Step 
# 2.Step 2: Check if that year is divisible by 100 (Year ÷ 100 leaves a remainder of 0). If no, it is a leap year. If yes, move to Step 3.
# Step 3: Check if that year is divisible by 400 (Year ÷ 400 leaves a remainder of 0). If yes, it is a leap year. If no, it is a normal year.

# def get_leap_year(year:int):
#     if year % 4 == 0: # 8 7
#         if year % 100 == 0: # 200, 204
#             if year % 400 == 0:
#                 print("It's a leap year")
#             else:
#                 print("It's a normal year")
#         else:
#             print("It's a leap year")
#     else:
#         print("Not a Leap year")


# get_leap_year(2204)

# 5. Write a function that receives a list of numbers and returns how many numbers are even.

# def get_total_even(numbers:list):
#     even_count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even_count += 1
#         else:
#             continue
#     print(f"The total number of even numbers in {numbers} is {even_count}.")

# get_total_even([4, 16, 20, 21, 3, 17, 22, 14, 67])

# 3. Write a function that receives a sentence and returns the sentence with all vowels removed.

# def strip_vowels(sentence:str):
#     vowels = "aeiou"
#     strip_sentence = ""
#     for i in sentence:
#         if i.lower() in vowels:
#             continue
#         else: # banana
#             strip_sentence += i
#     print(strip_sentence)

# strip_vowels("Banana")

# def strip_consonant(sentence:str):
#     vowels = "aeiou"
#     strip_sentence = ""
#     for i in sentence:
#         if i.lower() in vowels:
#             strip_sentence += i
#         else:
#             continue
#     print(strip_sentence)

# strip_consonant("Banana")

# 1. Write a function that receives principal, rate, and time and returns the simple interest.

def calculate_simple_interest(principal:float, rate:float, time:float):
    simple_interest = (principal * rate * time)
    print(simple_interest)

calculate_simple_interest(50000, 0.5, 1)
calculate_simple_interest(16000000, 0.49, 2)


# 2. Write a function that receives five numbers and returns the second largest number.

def get_second_largest_number(numbers:list):
    largest = max(numbers)
    second_largest = min(numbers)
    for i in numbers:
        if i > second_largest and i < largest:
            second_largest = i
        else:
            continue
    print(second_largest)

get_second_largest_number([32, 48, 62, 15, 94, 97, 119, 180])

# [32, 48, 62, 15, 94, 119]

# largest =119
# second_largest = 94

users = ["admin", "olamide", "joseph"]
symbols = "@!#%^*()__+~!<>?"
def validate_username(username:str):
    if username in users:
        print("Username already taken.")
    else:
        print("Username is available")
# username
# password

def validate_password(password:str):
    min_length = 8

    if len(password) >= min_length:
        if password.isalnum():
            print("Password is good")
        else:
            print("password needs to be alhpa-numeric")
    else:
        print("Password must be atleast 8 characters")
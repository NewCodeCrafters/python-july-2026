# first_name="nuhu"
# last_name="muhammad"
# sentence=f"my full name is{first_name}" "{last_name}"
# print ("sentence")


# favoritecity ="badagry"
# print("favoritecity")

# favoritecity=favoritecity.upper()
# print("favoritecity")

# favoritecity=favoritecity.lower()
# print("favoritecity")

# favoritecity=favoritecity.title()
# print("favoritecity")



# name =input("what is your name ")
# yob=int(input("enter your {yob} "))
# yob=2026-yob 
# numbers=int(input("enter two numbers of your choice {numbers} "))
# numbers= numbers+numbers
# birthyear=int(input("enterr your {birthyear} "))
# birthyear=2026-birthyear

# sentence=f"your name is {name} you are {yob} these numbers you picked {numbers} your birthyear is {birthyear}"
# print("sentence")


# def run_subtraction_calculator():
#     # loop until user enters correct numbers
#     while True:
#         # get inputs from user
#         first_num = input("Enter the starting number: ")
#         second_num = input("Enter the number to subtract: ")
        
#         # check if inputs are numbers
#         if first_num.replace('.', '', 1).isdigit() and second_num.replace('.', '', 1).isdigit():
#             x = float(first_num)
#             y = float(second_num)
            
#             # do subtraction
#             result = x - y
            
#             # print answer
#             print("The difference when subtracting", y, "from", x, "is", result)
#             break  # stop the loop
#         else:
#             print("Error: Please enter only numbers")
#             print()


# # run the function
# run_subtraction_calculator()



# # ## Exercise 7 – Vowel or Consonant Muhammed

# # Ask the user to enter a single letter.

# # Determine whether it is:

# # * A vowel
# # * A consonant

# letter =input("enter a single letter: ")
# if letter  in "aeiou" :
#     print (f"it is a vowel letter{letter}")
# else :
#     print ((f"it is a consonant {letter}"))


# # ## Exercise 14 – Lucky Number

# # Generate a random number between **1 and 20**.

# # Ask the user for a number.

# # Print:

# # * Lucky!
# # * Better luck next time.

# range =(1,20)
# lucky_number =input("enter a numer {lucky}: ")

# if lucky_number >= 20 :
#     print(f"you found the lucky number which is {lucky_number}: ")

# else :
#     print(f"no it is {lucky_number}: ")



# # ## Exercise 17 – Number Range

# # Generate a random number between **1 and 100**.

# # Ask the user for a number.

# # Print:

# # * Too High
# # * Too Low
# # * Correct


# range=(1,100)
# numbers=int(input("enter a number"  ))

# if numbers > 100:
#     print(f"too high")
# elif numbers < 0:
#     print(f"is too low")
# else :
#     print(f"it is correct")

# #     ## Exercise 24 – Movie Ticket

# # Ask the user for their age.

# # # Print the ticket category:

# # # * Child
# # # * Teen
# # # * Adult
# # # * Senior

# # age=int(input("enter your age: "))
# # if age < 13 :
# #     print(f"a child")
# # elif age > 13 :
# #     print(f"a teen")
# # elif age >= 18 :
# #     print (f"an adult")
# # else :
# #     print(f"senior man")



# # #     ## Exercise 27 – Number Comparison

# # # Ask the user for three numbers.

# # # Print:

# # # * Largest
# # # * Smallest

# # number1=(1,8,9)
# # numbers=int(input("enter three numbers "))
# # if numbers > numbers :
# #     print (f"largest")
# # else :
# #     print(f"smallest")


# # ### Muhammed

# # # 1. Given:

# # #    ```python
# # #    names = ["Uthman", "Emmanuel", "Muhammed", "Destiny", "Ayomide", "Maleek", 90, True, 192.12]
# # #    nums = [13, 12, 92, 13, "Love", "Demon"]
# # #    words = [names, nums]
# # #    ```

# # #    Write a statement to access the string `"Love"` using the `words` list.

# # # 2. Write the code to sort the `names` list in reverse alphabetical order after removing all non-string values.

names = ["Uthman", "Emmanuel", "Muhammed", "Destiny", "Ayomide", "Maleek", 90, True, 192.12]
nums = [13, 12, 92, 13, "Love", "Demon"]
words = [names, nums]
print ("[1][4]")
names.sorted("names[::-1]")
print("names")
names.remove(90)
names.remove(192.12)
names.remove(True)
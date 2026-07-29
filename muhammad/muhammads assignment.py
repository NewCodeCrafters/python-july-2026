first_name="nuhu"
last_name="muhammad"
sentence=f"my full name is{first_name}" "{last_name}"
print ("sentence")


favoritecity ="badagry"
print("favoritecity")

favoritecity=favoritecity.upper()
print("favoritecity")

favoritecity=favoritecity.lower()
print("favoritecity")

favoritecity=favoritecity.title()
print("favoritecity")



name =input("what is your name ")
yob=int(input("enter your {yob} "))
yob=2026-yob 
numbers=int(input("enter two numbers of your choice {numbers} "))
numbers= numbers+numbers
birthyear=int(input("enterr your {birthyear} "))
birthyear=2026-birthyear

sentence=f"your name is {name} you are {yob} these numbers you picked {numbers} your birthyear is {birthyear}"
print("sentence")


def run_subtraction_calculator():
    # loop until user enters correct numbers
    while True:
        # get inputs from user
        first_num = input("Enter the starting number: ")
        second_num = input("Enter the number to subtract: ")
        
        # check if inputs are numbers
        if first_num.replace('.', '', 1).isdigit() and second_num.replace('.', '', 1).isdigit():
            x = float(first_num)
            y = float(second_num)
            
            # do subtraction
            result = x - y
            
            # print answer
            print("The difference when subtracting", y, "from", x, "is", result)
            break  # stop the loop
        else:
            print("Error: Please enter only numbers")
            print()


# run the function
run_subtraction_calculator()
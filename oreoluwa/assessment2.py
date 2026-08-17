#Exercise 1: Function that receives a name and prints a greeting message
def person_name(name):
    print (f"Hello {name}")
name = input("Enter your name:")

person_name(name)



#Exercise 2: Function that receives a number and prints all numbers from 1 to that number
def print_number(n):
    num = 1
    while num <= n:
        print(num)
        num += 1

n = int(input("Enter a number: "))

print_number(n)


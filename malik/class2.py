# Write a function that receives two numbers and prints their sum.

def print_sum(num1,num2):
    total =(num1 + num2)
    print(total)
print_sum(5,7)

# Write a function that receives one number and prints **Even** if the number is even, otherwise print **Odd**.
def check_even_odd(num):
    if num % 2 == 0:
        print(num)
    else:
        print("Odd")
check_even_odd(4)
check_even_odd(7)



 #EXERCISE 1

num1 = float(input("Enter the first number: "))


num2 = float(input("Enter the second number: "))   

if num1 > num2:
    print(f"{num1} is the large number")

elif num1 < num2:
    print(f"{num2} is the large number")

else:
    print("Both numbers are equal") 


 # EXERCISE 2
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of the rectangle is: {area}")


#XERCISE 3
temp  = float(input("Enter the temperature in Celsius: "))  

fahrenheit = (temp * 9/5) + 32

print(f"The temperature in Fahrenheit is: {fahrenheit}")

# EXERCISE 4
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print(f"The average of the three numbers is: {average}")
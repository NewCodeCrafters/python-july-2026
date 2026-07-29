# Ayomide

### Exercise 1

# Ask the user to enter the price of one notebook.

### Exercise 2

# Ask the user to enter how many notebooks they want to buy.

### Exercise 3

# Calculate the total price.

### Exercise 4

# Ask the user to enter the amount they paid and calculate the balance they should receive.

price = float(input("Enter the price of one notebook: "))
quantity = int(input("enter the quantity of notbooks u want to buy: "))
Amount_paid = float(input("Enter the amount you paid: "))

total = float(price * quantity)
balance = float(Amount_paid - total)
print(total)

if Amount_paid > total:
    print(balance)
def run_division_calculator():
    while True:
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))

            if denominator == 0:
                print("Error: The denominator cannot be zero. Enter a new denominator.")
                continue

            result = numerator / denominator
            print(f"The result of {numerator} divided by {denominator} is {result}")
            break

        except ValueError:
            print("Error: Invalid Input, Enter correct values.")
            


# Run the calculator
run_division_calculator()
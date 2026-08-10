def run_multiplication_calculator():
    """Repeatedly prompts for two factors, multiplies them, and displays the product."""
    while True:
        try:
            input1 = input("Enter the first factor: ")
            input2 = input("Enter the second factor: ")
            x = float(input1)
            y = float(input2)
            product = x * y
            print(f"The product of {x} and {y} is: {product}.")
            break
        except ValueError:
            print("Error: invalid numeric input. Please try again.\n")
def run_area_calculator():
    while True:
        try:
            width = float(input("Enter the width of the rectangle: "))
            length = float(input("Enter the length of the rectangle: "))

            if width <= 0 or length <= 0:
                print("Width and length must be positive numbers. Please try again.\n")
                continue

            area = width * length

            print(f"The area of a rectangle with width {width} and length {length} is {area}")
            break

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


# Run the program
run_area_calculator()


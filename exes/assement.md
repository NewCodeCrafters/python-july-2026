# Python Programming Practical Assignment
**Topic:** Functions, Loops, Input Validation, and Exception Handling  
**Course Module:** Introduction to Python Logic  

---

## Instructions for All Students

Read the instructions carefully. Complete your assigned task individually. Do not copy code from online sources or peers.

### General Requirements
1. **No Code Copying:** Write all code independently based on concept logic.
2. **Structure:**
   - Define a custom function to hold your logic.
   - Implement continuous input prompting using a loop.
   - Use `try` and `except` blocks to handle invalid inputs (e.g. text entered instead of numbers).
   - Perform the required mathematical operation.
   - Exit the loop cleanly upon successful calculation.
3. **Testing:**
   - Test your function with valid numbers.
   - Test your function with invalid input (e.g. typing words) to ensure it handles errors without crashing.

---

## Individual Assignments

### Person 1: Addition Calculator
* **Objective:** Create a program that repeatedly prompts the user for two numbers, adds them together, and displays the sum.
* **Requirements:**
  1. Define a function named `run_addition_calculator()`.
  2. Prompt the user for a first number and a second number.
  3. Convert both inputs to floating-point numbers.
  4. If conversion fails (user enters letters), display an error message and repeat the prompt.
  5. Print the formatted result: `The sum of X and Y is Z`.
  6. Break out of the loop after a successful calculation.

---

### Person 2: Subtraction Calculator
* **Objective:** Create a program that repeatedly prompts the user for two numbers, subtracts the second from the first, and displays the difference.
* **Requirements:**
  1. Define a function named `run_subtraction_calculator()`.
  2. Prompt the user for the starting number and the number to subtract.
  3. Convert both inputs to numeric values.
  4. Handle input errors using `try`/`except` so invalid entries do not terminate the script.
  5. Print the formatted result: `The difference when subtracting Y from X is Z`.
  6. Terminate the loop after printing the answer.

---

### Person 3: Multiplication Calculator
* **Objective:** Create a program that repeatedly prompts the user for two numbers, multiplies them, and displays the product.
* **Requirements:**
  1. Define a function named `run_multiplication_calculator()`.
  2. Prompt the user for two factors.
  3. Use input conversion and error catching to handle invalid string inputs safely.
  4. Multiply the two numbers together.
  5. Print the formatted result: `The product of X and Y is Z`.
  6. Stop execution of the prompt loop after a successful run.

---

### Person 4: Division Calculator
* **Objective:** Create a program that prompts for two numbers, divides the first by the second, and handles both text errors and division by zero.
* **Requirements:**
  1. Define a function named `run_division_calculator()`.
  2. Prompt the user for a numerator and a denominator.
  3. Use `try`/`except` to handle non-numeric inputs.
  4. Add validation or exception handling to prevent division by zero (print a friendly error if denominator is zero).
  5. Print the formatted result: `The result of X divided by Y is Z`.
  6. Exit the loop once a valid division is completed.

---

### Person 5: Rectangle Area Calculator
* **

---

### Person 6: Rectangle Perimeter Calculator
* **Objective:** Create a program that calculates the perimeter of a rectangle using user-provided dimensions.
* **Requirements:**
  1. Define a function named `run_perimeter_calculator()`.
  2. Prompt the user for width and length values.
  3. Use `try`/`except` to prevent crashes when non-numeric input is provided.
  4. Validate that dimensions are greater than zero.
  5. Calculate perimeter (`2 * (width + length)`) and print: `The perimeter of a rectangle with width X and length Y is Z`.
  6. Exit the loop cleanly after completion.

---

## Submission Criteria

| Task | Total Points |
| :--- | :--- |
| Proper Function Definition & Calling | 20% |
| Input Loop Implementation | 20% |
| Exception Handling (`try`/`except`) | 30% |
| Correct Mathematical Logic & Output Formatting | 30% |
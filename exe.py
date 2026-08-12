
# ### 🔄 For Loop Exercises — 16–22

# 16. **Print a Word Multiple Times**
#     Ask the user to enter a word and print that word **5 times** using a `for` loop.

word = input("Enter your jargon here: ")

for i in range(1, 6):
    print(word)


# 17. **Sum List Numbers**
#     Given:

#     ```python
#     numbers = [10, 20, 5, 15, 30]
#     ```

#     Use a `for` loop to calculate and print the total.

numbers = [10, 20, 5, 15, 30]
total = 0

for i in numbers:
    total += i

print(total)

# 18. **Find the Largest Number**
#     Given:

#     ```python
#     numbers = [12, 45, 7, 89, 23, 56]
#     ```

#     Use a `for` loop to find and print the largest number.
numbers = [12, 45, 7, 89, 23, 56]
largest = 0

for i in numbers:
    if i > largest:
        largest = i
    else:
        continue

print(largest)

print(max(numbers))

# 19. **Count Vowels**
#     Ask the user to enter a word. Use a `for` loop to count how many vowels (`a`, `e`, `i`, `o`, `u`) are in the word.

word = input("Enter your jargon: ")

vowels = "aeiou"
vowel_count = 0

for i in word:
    if i.lower() in vowels:
        vowel_count += 1
    else:
        continue

print(vowel_count)


# 20. **Print Characters**
#     Ask the user to enter a word. Use a `for` loop to print each character on a separate line.
word = input("Enter your jargon: ")

for i in word:
    print(i)


# 21. **Calculate Squares**
#     Use a `for` loop to print the square of every number from **1 to 10**.

for i in range(1, 11):
    print(i ** 2)


# 22. **Count Positive Numbers**
#     Given:

#     ```python
#     numbers = [-5, 10, -2, 7, 0, 15, -8, 3]
#     ```

#     Use a `for` loop to count how many numbers are **positive**.
numbers = [-5, 10, -2, 7, 0, 15, -8, 3]

number_count = 0

for number in numbers:
    if number > 0:
        number_count += 1
    else:
        continue

print(number_count)


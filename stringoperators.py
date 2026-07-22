# = Assignment operator
# It is used to store a value inside a variable.

# + String concatenation operator
# It joins two or more strings together.

# Store the first name in a variable
first_name = "OlAmidE BeLLo"

# Slicing: Extract characters from index 8 up to (but not including) index 13.
# Index:  0123456789012
# String: OlAmidE BeLLo
# Output: "BeLLo"
print(first_name[8:13])

# Slicing with a step value.
# Syntax: string[start:stop:step]
# Start from the beginning, stop before index 8,
# and take every 2nd character.
# Output: "OAmd"
print(first_name[:8:2])

# Store the last name
last_name = "Bello"

# Reverse the string using slicing.
# [::-1] means:
# Start from the end, move backwards one character at a time.
# Output: "olleB"
print(last_name[::-1])

# Concatenate (join) strings together.
# full_name = first_name + " " + last_name
# print(full_name)  # Output: OlAmidE BeLLo Bello

# f-string (formatted string) allows variables to be inserted into strings.
# sentence = f"My name is {full_name}"
# print(sentence)

# =====================
# String Methods
# =====================

# Convert every character to uppercase.
# first_name = first_name.upper()
# print(first_name)

# Convert every character to lowercase.
# first_name = first_name.lower()
# print(first_name)

# Capitalize the first letter of every word.
# first_name = first_name.title()
# print(first_name)

# Capitalize only the first character of the string.
# first_name = first_name.capitalize()
# print(first_name)

# =====================
# Indexing and Slicing
# =====================

# Indexing starts from 0.
# Positive indexing moves from left to right.
# Negative indexing moves from right to left.

# Print the character at index 12.
# print(first_name[12])

# Print the 5th character from the end.
# print(first_name[-5])

# Slice from index 0 up to (but not including) index 2.
# Output: "Ol"
# print(first_name[0:2])
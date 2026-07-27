# Ayomide
# Exercise 1
First_name = "Akapo"
Middle_name = "Ayomide"
Last_name = "Sewanu"

# Join in one sentence
sentence = f"My Full name is {First_name} {Middle_name} {Last_name}"
print(sentence)

# Exercise 2

# Print:
# Welcome, <full name>
# using an f-string.
Full_name = f"{First_name} {Middle_name} {Last_name}"
print(f"Welcome, {Full_name}")

### Exercise 3
# Print only the initials of the three names using indexing.
initials = f"{First_name[0]}. {Middle_name[0]}. {Last_name[0]}"
print(f"Initials = {initials}")

### Exercise 4
# Print the full name in reverse order (characters reversed).
reversed_name = Full_name[::-1]
print(f"Reversed name: {reversed_name}")

import random

def save_student_name():
    name = input("Enter your name here: ")
    with open("students.txt", "a") as file:
        file.write(f"{name}\n")

    print(f"{name} saved to students.txt")

# save_student_name()

def read_student_name():
    with open('students.txt', 'r') as file:
        print(file.readlines())


# read_student_name()

# 3. Random Student Picker — Beginner/Intermediate

# Create a program that:

# Reads student names from students.txt.
# Randomly selects one student.
# Displays the selected student.
# Saves the selected student's name inside selected_students.txt.

# Do not manually create a Python list containing the names.

def select_and_save_random_name():
    with open('students.txt', "r") as file:
        temp = file.readlines()

    with open('selected_student.txt', "a") as doc:
        rand_name = random.choice(temp)
        doc.write(rand_name)
        
# select_and_save_random_name()


def select_and_save_two_random_names():
    with open('students.txt', "r") as file:
        temp = file.readlines()

    with open('selected_student.txt', "a") as doc:
        rand_name = random.choices(temp, k=2)
        for i in rand_name:
            doc.write(i)
        
def save_student_name():
    name = input("Enter your name here: ")
    with open("/Users/user/dev/python-july-2026/student_app/students.txt", "a") as file:
        file.write(f"{name}\n")

    print(f"{name} saved to students.txt")

def read_student_name():
    with open('/Users/user/dev/python-july-2026/student_app/students.txt', 'r') as file:
        print(file.readlines())


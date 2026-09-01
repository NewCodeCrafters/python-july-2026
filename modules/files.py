# # docs = open("modules/text.txt", mode="r")

# # print(docs.read())

# # docs.close()

# # context manager

# # with open("modules/text.txt", mode="r") as docs:
# #     print(docs.read())

# with open("output.txt", "w") as file:
#     file.write("Hello, World!\t\t\t")
#     file.write("This is a new line.")


# Task: Write a script that asks the user to input their thoughts for the day. Save this input into a file named journal.txt.

# sentence = input("Enter your thoughts for the day: ")

# with open("journals.txt", 'a') as docs:
#     docs.write(f"\n{sentence}")

# .read()
# readlines() []

with open("journals.txt", "r") as docs:
    items = docs.readlines()
    for i in items:
        if "Garri" in i:
            print(i)
        else:
            continue

with open("journals.txt", "r") as docs:
    items = docs.read()
    items = items.split()
    print(len(items))

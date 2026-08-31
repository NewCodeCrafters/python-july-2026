# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")
score = int(input("Enter your score: "))
if score >= 75 and score <= 100:
    print("You got an A1")
elif score >= 70 and score < 74:
    print("You got a B2")
elif score >= 65 and score < 69:
    print("You got a B3")
elif score >= 60 and score < 64:
    print("You got a C4")
elif score >= 55 and score < 59:
    print("You got a C5")
elif score >= 50 and score < 54:
    print("You got a C6")
elif score >= 45 and score < 49:
    print("You got a D7")
elif score >= 40 and score < 44:
    print("You got an E8")
elif score >= 0 and score < 39:
    print("You got an F9")
else:
    print("Invalid score")

correct_password = "secure123"
max_attempts = 3
attempts_left = max_attempts


while True:
    password = str(input("Enter your password:"))
    if password == correct_password:
        print("Access granted")
        break
    else:
         attempts_left -= 1
         if attempts_left > 0:
                print(f"Incorrect password. You have {attempts_left} attempts left.")
         else:
              print("You have run out of attempts")    









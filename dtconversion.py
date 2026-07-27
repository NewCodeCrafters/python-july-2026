# We can convert int to fugyloat, string, and boolean
# 42 can be "42" or 42.0 or True

# We can convert strings to float, int, and boolean
# "3.14" can be 3.14 or 3 or True
# We can't convert string characters to numeric datatype e.g "A"

# We can convert booleans to int, float, and string
# True can be 1 or 1.0 or "True"

# Example code
num = 42
print(float(num))      # 42.0
print(str(num))        # "42"
print(bool(num))       # True

value = "3.14"
print(float(value))    # 3.14
print(int(float(value)))  # 3
print(bool(value))     # True

flag = True
print(int(flag))       # 1
print(float(flag))     # 1.0
print(str(flag))       # "True"


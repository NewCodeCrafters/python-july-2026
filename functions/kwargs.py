def add_numbers(*nums): # argument
    return sum(nums)

def subtraction(num1, num2):
    return num1 - num2


def perform_operation(num1, num2, operator):
    if operator == "+":
        return add_numbers(num1, num2)
    elif operator == "-":
        return subtraction(num1, num2)
    else:
        return "Invalid Statement"

num_list = [i for i in range(1, 11)]

# for i in range(1, 11):
#     num_list.append(i)

print(num_list)
# total = add_numbers(12, 13, 15, 19)
# print(total)


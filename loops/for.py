names = ["Uthman", "Emmanuel", "Muhammed", "Destiny", "Ayomide", "Maleek", "Justice", "Hakeem", "John"]

# for name in names:
#     print(name)

# 1 - 10

# for i in range(30): start 0 end 29
# for num in range(2, 21, 2): # starts 1 and end 49, 2 steps
#     print(num)

name = input("Enter your name here: ")

vowels = "aeiou"

counts = 0
vowel_list = []

for i in name:
    if i.lower() in vowels:
        counts += 1
        vowel_list.append(i)
    else:
        continue

print(f'There are {counts} vowels in {name}')

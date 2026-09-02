# [] () {} {}

# key and value pairs
students = {
    "bsu/math/005": ["Maleek", 23, "Male", "Cyber Security"],
    "unn/com/991": "Ayomide",
}


names = {
    "oldnewdev": "AbdulHakeem",
    "item7go": "Uthman",
    "elephant": "Muhammed",
    "justyp": "Justice",
    "Destro": "Destiny",
}

departments = {
    "kiss or grab": "Mass Communication",
    "Podcast Managers": "Theatre art",
    "farmers": "Agric Education"
}

bigger_item = {
    "names": names,
    "departments": departments
}

# Dictionaries cannot be indexed but can use key to get value
# Dictionary keys are unique
print(students.get("unn/com/991"))
print(students.items())

# FIFO
print(bigger_item.get("names").get("item7go"))
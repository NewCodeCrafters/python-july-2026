# What is OOP?
# Importance
# Syntax in Python
# Benefits
# Attributes of OOP

class Animal:
    ...

class Animal:
    # methods
    # built in methods & custom methods
    def __init__(self, name, types, kind):
        self.name = name
        self.types = types
        self.kind = kind

    def __str__(self):
        return f"This is a {self.name}"

    def get_attributes(self):
        return "I am an Animal"


# Object of Animal
dog = Animal(name="Dog", types="Cold Blooded", kind="Domestic")
cat = Animal(name="Cat", types="Cold Blooded", kind="Domestic")

# print(dog)
# print(cat)

class LibraryBook:
    def __init__(self, title:str, author:str, isbn:int, pub_year:int, genre:str, total_copies:int, available_copies:int, borrow_counts:int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pub_year = pub_year
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.borrow_counts = borrow_counts


    def __str__(self):
        if self.available_copies > 0:
            return f"Book name is {self.title} by {self.author}. It is in Stock"
        else:
            return f"Book name is {self.title} by {self.author}. It is Out of Stock"
            
    
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.borrow_counts += 1
            return f"Book borrowed from Library successfully. Available copy is now {self.available_copies}"
        else:
            return f"No books available to be borrowed"


book1 = LibraryBook(title="Things Fall Apart", author="Chinua Achebe", isbn=21673737, pub_year=1962, genre="Drama", total_copies=30, available_copies=30, borrow_counts=0)

print(book1)
print(book1.borrow())


# 2. Library Management

# # Classes: Book, Member, Loan, Library

# # Tests: borrowing rules, due dates, availability tracking

# # Watch for: Is Library a god class? Do Book and Member actually hold their own state?


# 1. Identify the Core Concepts (Domain Modeling)
# Start by asking: what real-world things exist and what do they know or do?

# Book – A physical or logical item that can be borrowed.
# It has identity (title, author, ISBN, unique copy ID) and a current status (available or not).
# Member – A person who can borrow books.
# It has identity (name, member ID) and a history or limit of what they currently hold.
# Loan – The act of borrowing itself.
# This is the relationship that connects a specific Book to a specific Member for a period of time. It carries the due date and the actual borrow/return timestamps.
# Library – The system that coordinates everything.
# It knows about all books and all members and provides the operations people actually use (borrow, return, search, check overdue, etc.).

class Book:
    def __init__(self, book_id, title, author, total_copies, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies
       
        
        
    def __str__(self):
        if self.available_copies > 0:
            return f"Book name is {self.title} by {self.author}. It is in Stock"
        else:
            return f"Book name is {self.title} by {self.author}. It is Out of Stock"

    def book_info(self):
         return f"The title of the book is {self.title} and it's written by {self.author},total copies available is {self.total_copies}"
                    

class Member():
    def __init__(self, member_id, name):
         self.member_id = member_id
         self.name = name

    def member_info(self):
         return f"member id is {self.member_id}, name is {self.name}"

class Loan():
    def __init__(self, borrow_counts):
         self.borrow_counts = borrow_counts

    def borrow(self):
        self.borrow_counts = 0
        if self.available_copies > 0:
            self.available_copies -= 1
            self.borrow_counts += 1
            return f"Book borrowed from Library successfully. Available copy is now {self.available_copies}"
        else:
            return f"No books available to be borrowed"
    

class Library():
     def is_available(self):
        if self.available_copies == True:
            return "Book is available"
        else:
            return "Book is not available"
    

book1 = Book(title="The lion and the jewel", author="JOHN",book_id=1001, total_copies=30, available_copies=30)
print(book1.book_info())
print(book1)
m = Member(501, "Ada")
print(m.member_info())
# loan = Loan( "The lion and the jewel")
# print(loan.borrow())
# lib = Library(1001, "The lion and the jewel", "JOHN", 30, 30, 0)
# print(lib.is_available())







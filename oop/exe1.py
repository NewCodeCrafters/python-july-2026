class Book:

    def __init__(self, title, author, isbn, publication_year):
        self._is_borrowed = False
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def borrow(self):
        if self._is_borrowed:
            print("Book is already borrowed")
        else:
            self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

    def get_status(self):
        if self._is_borrowed == True:
            return "Book is already borrowed"
        else:
            return "Book is available"

    def display_info(self):
        return f"Book name is {self.title}. The author's name is {self.author}. The ISBN is {self.isbn}. The publication year is {self.publication_year}"

tfa = Book(title="Things Fall Apart", author="Chinua Achebe", isbn=21327833243, publication_year=1973)
print(tfa.get_status())
tfa.borrow()
tfa.borrow()
tfa.return_book()
print(tfa.get_status())
# print(tfa.get_status())
print(tfa.display_info())

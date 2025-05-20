class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []

    def borrow(self, book):
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.__name} borrowed '{book._Book__title}'")
        else:
            print("Book not available.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.__name} returned '{book._Book__title}'")

class Student(Member):
    pass

class Faculty(Member):
    pass

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title  # Private variable (encapsulation)
        self.__author = author
        self.__isbn = isbn
        self.__available = True

    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Available: {self.__available}")

    def is_available(self):
        return self.__available

    def borrow_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

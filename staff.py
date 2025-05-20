class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} added '{book._Book__title}' to the library.")

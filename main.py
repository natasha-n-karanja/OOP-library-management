def main():
    library = Library()
    staff = Staff("Alice", "Librarian")
    member = Student("John Doe", "S123")

    # Create books
    book1 = Book("1984", "George Orwell", "12345")
    book2 = Book("Python Basics", "Jane Smith", "67890")

    # Add books
    staff.add_book(library, book1)
    staff.add_book(library, book2)

    while True:
        print("\n1. View Books\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            library.show_books()
        elif choice == '2':
            member.borrow(book1)
        elif choice == '3':
            member.return_book(book1)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

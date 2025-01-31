# Let's create the `Book` and `LibraryMember` classes as described, with the necessary attributes and methods.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        """Marks the book as borrowed."""
        self.is_borrowed = True

    def mark_as_returned(self):
        """Marks the book as returned."""
        self.is_borrowed = False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """Allows the member to borrow a book if it's available."""
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently unavailable.")

    def return_book(self, book):
        """Allows the member to return a book they have borrowed."""
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has successfully returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' in their borrowed books.")

    def list_borrowed_books(self):
        """Lists all books the member has borrowed."""
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")



book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

member = LibraryMember("Alice", "M001")

def interact_with_library():
    while True:
        print("\nLibrary Menu:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable books to borrow:")
            books = [book1, book2, book3]
            available_books = [book for book in books if not book.is_borrowed]
            if available_books:
                for i, book in enumerate(available_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                book_choice = int(input("Enter the book number to borrow: ")) - 1
                if 0 <= book_choice < len(available_books):
                    member.borrow_book(available_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("No books are available to borrow.")
        
        elif choice == "2":
            print("\nBorrowed books:")
            if member.borrowed_books:
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                book_choice = int(input("Enter the book number to return: ")) - 1
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("You have no books to return.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive library system
interact_with_library()

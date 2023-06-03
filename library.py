class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book found: {book.title} by {book.author}")
                return
        print("Book not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"{book.title} by {book.author}")

# Creating a library object
library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        book = Book(title, author, isbn)
        library.add_book(book)
        print("Book added successfully.")
    elif choice == '2':
        title = input("Enter the title of the book to remove: ")
        book = library.search_book(title)
        library.remove_book(book)
    elif choice == '3':
        title = input("Enter the title of the book to search: ")
        library.search_book(title)
    elif choice == '4':
        library.display_books()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

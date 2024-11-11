class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.year_published}"

class FictionBook(Book):
    def __init__(self, title, author, isbn, year_published, genre):
        super().__init__(title, author, isbn, year_published)
        self.genre = genre

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Genre: {self.genre}"

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, year_published, topic):
        super().__init__(title, author, isbn, year_published)
        self.topic = topic

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Topic: {self.topic}"

class ReferenceBook(Book):
    def __init__(self, title, author, isbn, year_published, description):
        super().__init__(title, author, isbn, year_published)
        self.description = description

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Description: {self.description}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} has been removed.")
                return
        print(f"No book found with ISBN {isbn}.")

    def get_books(self):
        return [book.get_info() for book in self.books]

    def get_books_by_category(self, category):
        if category == "Fiction":
            return [book.get_info() for book in self.books if isinstance(book, FictionBook)]
        elif category == "NonFiction":
            return [book.get_info() for book in self.books if isinstance(book, NonFictionBook)]
        elif category == "Reference":
            return [book.get_info() for book in self.books if isinstance(book, ReferenceBook)]
        else:
            return f"No books found in the category '{category}'"

    def get_books_by_author(self, author):
        return [book.get_info() for book in self.books if book.author == author]

    def get_books_by_year(self, year):
        return [book.get_info() for book in self.books if book.year_published == year]

if __name__ == "__main__":
    library = Library()

    book1 = FictionBook("Of mice and men", "Jon Steynbek", "9780140177398", 1937, "Tragedy")
    book2 = NonFictionBook("A brief history of time", "Stiven Hawking", "9783644008618", 1988, "Physics")
    book3 = ReferenceBook("Encyclopedia of Science", "John Doe", "1122334455", 2000,
                          "A comprehensive guide to science.")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("\nAll books in the library:")
    print("\n".join(library.get_books()))

    print("\nFiction books in the library:")
    print("\n".join(library.get_books_by_category("Fiction")))

    print("\nNonFiction books in the library:")
    print("\n".join(library.get_books_by_category("NonFiction")))

    print("\nBooks by author 'Stiven Hawking':")
    print("\n".join(library.get_books_by_author("Stiven Hawking")))

    print("\nBooks published in 1937:")
    print("\n".join(library.get_books_by_year(1937)))

    library.remove_book("9780140177398")
    print("\nAll books in the library after removal:")
    print("\n".join(library.get_books()))


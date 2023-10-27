class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        author.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library {self.name} with books: {self.books}"

    def __str__(self):
        return self.__repr__()


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"{self.name} from {self.country}"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # Создаем библиотеку и авторов
    library = Library("Central Library")
    author1 = Author("Leo Tolstoy", "Russia", "1828-09-09")  # Изменил страну
    author2 = Author("George Orwell", "UK", "1903-06-25")

    # Добавляем книги
    book1 = library.new_book("War and Peace", 1869, author1)
    book2 = library.new_book("1984", 1949, author2)
    book3 = library.new_book("Animal Farm", 1945, author2)

    # Выводим информацию о библиотеке
    print(library)

    # Выводим книги по авторам
    print(f"Books by Leo Tolstoy: {library.group_by_author(author1)}")
    print(f"Books by George Orwell: {library.group_by_author(author2)}")

    # Выводим книги по году
    print(f"Books from 1945: {library.group_by_year(1945)}")

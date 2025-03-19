class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_info(self):
        return f'{self.name} ({self.birth_year})'


class Book:
    def __init__(self, title, year, annotation, author):
        self.title = title
        self.year = year
        self.annotation = annotation
        self.author = author

    def get_info(self):
        info = f'{self.title} ({self.year}) by {self.author.get_info()}'
        if self.annotation:
            info += f'\nAnnotation: {self.annotation}'
        return info


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if not any(b.title == book.title and b.author.name == book.author.name for b in self.books):
            self.books.append(book)

    def list_books(self):
        return [book.get_info() for book in self.books]

    def find_books_by_author(self, author_name):
        return [book.get_info() for book in self.books if book.author.name == author_name]
    
    def search_books_by_year(self, year):
        return [book.get_info() for book in self.books if book.year == year]

    def search_books_by_keywords(self, keywords):
        return [book.get_info() for book in self.books if any(keyword.lower() in book.title.lower() or 
                                                                      keyword.lower() in book.annotation.lower() for keyword in keywords)]




class Reader:
    def __init__(self, name):
        self.name = name
        self.rented_books = []

    def rent_book(self, book):
        if book not in self.rented_books:
            self.rented_books.append(book)

    def return_book(self, book):
        if book in self.rented_books:
            self.rented_books.remove(book)

    
# --- Тестуємо ---
author1 = Author("Іван Франко", 1856)
author2 = Author("Леся Українка", 1871)
author3 = Author("Тарас Шевченко", 1814)
book1 = Book("Захар Беркут", 1883, "Роман про боротьбу українців із загарбниками", author1)
book2 = Book("Лісова пісня", 1911, "Поема про кохання", author2)
book3 = Book("Кобзар", 1840, "", author3)
library = Library("Національна бібліотека")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print("📚 Книги в бібліотеці:")
print("\n".join(library.list_books()))

reader = Reader("Петро")
reader.rent_book(book1)
print("\n📖 Орендовані книги:")
print("\n".join([b.get_info() for b in reader.rented_books]))

reader.return_book(book1)
print("\n📖 Орендовані книги після повернення:")
print("\n".join([b.get_info() for b in reader.rented_books]) or "Немає орендованих книг.")

print("\n🔍 Пошук книг за роком:")
print("\n".join(library.search_books_by_year(1883)))

print("\n🔍 Пошук книг за ключовими словами ('Захар', 'боротьба'):")
print("\n".join(library.search_books_by_keywords(["Захар", "боротьба"])))


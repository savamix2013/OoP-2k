class Book:
    """Клас книги з інкапсуляцією"""
    def __init__(self, title, author, year, pages, genre):
        # Приватні атрибути книги
        self._title = title.title()
        self._author = author.title()
        self._year = year
        self._pages = pages
        self._genre = genre.title()
    
    def get_info(self):
        """Повертає інформацію про книгу у вигляді рядка"""
        return (f"Назва: {self._title}\n"
                f"Автор: {self._author}\n"
                f"Рік видання: {self._year}\n"
                f"Сторінок: {self._pages}\n"
                f"Жанр: {self._genre}\n"
                f"{self.is_modern()}\n"
                f"{'-'*30}")
    
    def is_modern(self):
        """Перевіряє, чи книга сучасна (видана після 2010 року)"""
        return self._year > 2010
    
    def compare_pages(self, other_book):
        """Порівнює дві книги за кількістю сторінок"""
        if self._pages > other_book._pages:
            return f"'{self._title}' має більше сторінок ({self._pages}), ніж '{other_book._title}' ({other_book._pages})."
        elif self._pages < other_book._pages:
            return f"'{other_book._title}' має більше сторінок ({other_book._pages}), ніж '{self._title}' ({self._pages})."
        else:
            return f"'{self._title}' і '{other_book._title}' мають однакову кількість сторін ({self._pages})."
    
    @property
    def title(self):
        """Властивість для отримання назви книги"""
        return self._title


class Library:
    """Клас бібліотеки, що інкапсулює список книг та методи для роботи з ними"""
    def __init__(self):
        self._books = []  # приватний список книг
    
    def add_book(self, book):
        """Додає книгу до бібліотеки"""
        self._books.append(book)
    
    def find_book(self, title):
        """Пошук книги за назвою"""
        title = title.title()  # уніфікація регістру
        for book in self._books:
            if book.title == title:
                return book.get_info()
        return "Книгу не знайдено"
    
    def show_all_books(self):
        """Виводить інформацію про всі книги в бібліотеці"""
        for book in self._books:
            print(book.get_info())


def main():
    # Створення об'єктів книг
    new_book1 = Book('python для початківців', 'джон до', 2015, 350, 'література')
    new_book2 = Book('гаррі поттер', 'дж. к. ролінг', 2007, 500, 'фентезі')
    new_book3 = Book('будинок старлінгів', 'алекс і. герроу', 2024, 480, 'жахи')
    
    # Створення бібліотеки та додавання книг
    library = Library()
    library.add_book(new_book1)
    library.add_book(new_book2)
    library.add_book(new_book3)
    
    # Вивід усіх книг
    library.show_all_books()
    
    # Інтерактивний цикл пошуку книги
    while True:
        user_input = input("Введіть назву книги (або 'q' для виходу): ")
        if user_input.lower() == 'q':
            print("Щасливо!")
            break
        print(library.find_book(user_input))
    
    # Приклади порівняння книг за кількістю сторінок
    print(new_book1.compare_pages(new_book2))
    print(new_book2.compare_pages(new_book3))


if __name__ == "__main__":
    main()

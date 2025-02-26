"""Клас книги в бібліотеці"""

class Book:
    """Описуємо книгу"""

    def __init__(self, title, author, year, pages, genre):
        """інціалізувати атрибути, що описують книжку"""
        self.title = title.title()
        self.author = author.title()
        self.year = year
        self.pages = pages
        self.genre = genre.title()
        
    
    def get_info(self):
        """Повертає інформацію про книгу у вигляді рядка"""
        return (f"Назва: {self.title}\n" 
                f"Автор: {self.author}\n"
                f"Рік видання: {self.year}\n"
                f"Сторінок: {self.pages}\n"
                f"Жанр: {self.genre}\n"
                f"{self.is_modern()}\n"
                f"{'-'*30}")


    def is_modern(self):
        """Перевіряє, чи книга сучасна (видана після 2010 року)."""
        return self.year > 2010
    

    def comparator_pages(self, other_book):
        """Метод порівняння двох книг за к-тю ст."""
        if self.pages > other_book.pages:
            return f"'{self.title}' має більше сторінок ({self.pages}), ніж '{other_book.title}' ({other_book.pages})."
        elif self.pages < other_book.pages:
            return f"'{other_book.title}' має більше сторінок ({other_book.pages}), ніж '{self.title}' ({self.pages})."
        else:
            return f"'{self.title}' і '{other_book.title}' мають однакову кількість сторін ({self.pages})."


                       
new_book1 = Book('python для початківців', 'джон до', 2015, 350, 'література')    
new_book2 = Book('гаррі поттер', 'дж. к. ролінг', 2007, 500, 'фентезі')
new_book3 = Book('будинок старлінгів', 'алекс і. герроу', 2024, 480, 'жахи')

print(new_book1.get_info())
print(new_book2.get_info())
print(new_book3.get_info())

books = [new_book1, new_book2, new_book3]


def find_book(books, title):
    """Пошук книги за назвою"""
    title = title.title()
    for book in books:
        if book.title == title:
            return book.get_info()
    return "Книгу не знайдено"


while True:
    user_writing = input("Введіть назву книги (або 'q' для виходу): ")
    if user_writing.lower() == 'q':
        print("Щасливо!")
        break
    print(find_book(books, user_writing))


print(new_book1.comparator_pages(new_book2))
print(new_book2.comparator_pages(new_book3))
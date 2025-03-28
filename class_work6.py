class Library:
    def __init__(self, name: str, address: str, year: int):
        self.name = name
        self.address = address
        self.year = year
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        return f"Бібліотека {self.name} за адресою {self.address} заснована у {self.year} році"
    

class Department:
    def __init__(self, name: str):
        self.name = name
        self.items = []  # Один список для всіх матеріалів

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, title):
        for item in self.items:
            if hasattr(item, "title") and item.title == title:
                self.items.remove(item)
                break

    def get_items(self):
        return [item.get_info() for item in self.items]

    def __str__(self):
        return f"Відділ {self.name}"
    

class Book:
    def __init__(self, title: str, year: int, author):
        self.title = title
        self.year = year
        self.author = author
        self.rating = Rating()

    def get_info(self):
        return f"{self.title} ({self.year}) by {self.author.get_info()}"

    def add_rating(self, user, rating, review):
        self.rating.add_rating(user, rating, review)

    def get_avg_rating(self):
        return self.rating.get_avg_rating()
    

class Author:
    def __init__(self, name: str, surname: str, birth_year: int):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.books = []

    def get_info(self):
        return f"{self.name} {self.surname} ({self.birth_year})"

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return [book.title for book in self.books]
    

class ElectronicBook(Book):
    def __init__(self, title: str, year: int, author, file_format: str, file_size: float):
        super().__init__(title, year, author)
        self.file_format = file_format
        self.file_size = file_size

    def get_info(self):
        return f"{super().get_info()} Формат: {self.file_format}, Розмір: {self.file_size} Мб"
    

class Reader:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def rent_book(self, book):
        if len(self.books) >= self.max_books():
            print(f"Користувач {self.name} досяг ліміту книг ({self.max_books()}).")
            return
        if book not in self.books:
            self.books.append(book)

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def max_books(self):
        return 5


class Student(Reader):
    def max_books(self):
        return 10


class Guest(Reader):
    def max_books(self):
        return 3


class Rating:
    def __init__(self):
        self.ratings = {}

    def add_rating(self, user, rating, review):
        self.ratings[user] = (rating, review)

    def get_avg_rating(self):
        if not self.ratings:
            return 0  # Повертаємо 0, якщо немає оцінок
        return sum(rating for rating, _ in self.ratings.values()) / len(self.ratings)


class MultimediaMaterial:
    def __init__(self, title: str, duration: int, year: int):
        self.title = title  # Змінено з name на title
        self.duration = duration
        self.year = year

    def get_info(self):
        return f"{self.title} {self.duration} хвилин {self.year} року"


class Video(MultimediaMaterial):
    def __init__(self, title: str, duration: int, year: int, genre: str):
        super().__init__(title, duration, year)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()} Жанр: {self.genre}"


class Audio(MultimediaMaterial):
    def __init__(self, title: str, duration: int, year: int, author: str, file_format: str):
        super().__init__(title, duration, year)
        self.author = author
        self.file_format = file_format

    def get_info(self):
        return f"{super().get_info()} Автор: {self.author}, Формат: {self.file_format}"


class PeriodicalPublication:
    def __init__(self, title: str, periodicity: str, publisher: str):
        self.title = title  # Змінено з name на title
        self.periodicity = periodicity
        self.publisher = publisher

    def get_info(self):
        return f"{self.title}, періодичність: {self.periodicity}, видавець: {self.publisher}"


class Newspaper(PeriodicalPublication):
    def __init__(self, title: str, periodicity: str, publisher: str, theme: str):
        super().__init__(title, periodicity, publisher)
        self.theme = theme

    def get_info(self):
        return f"{super().get_info()} Тематика: {self.theme}"


class Magazine(PeriodicalPublication):
    def __init__(self, title: str, periodicity: str, publisher: str, region: str):
        super().__init__(title, periodicity, publisher)
        self.region = region

    def get_info(self):
        return f"{super().get_info()} Регіон: {self.region}"


lesya_ukraine = Author("Леся", "Українка", 1871)
ivan_franko = Author("Іван", "Франко", 1856)

fiction_department = Department("Художня література")

fiction_department.add_item(Book("Лісова пісня", 1911, lesya_ukraine))
fiction_department.add_item(Book("Бояриня", 1910, lesya_ukraine))
fiction_department.add_item(ElectronicBook("Лісова пісня", 1911, lesya_ukraine, "PDF", 5.2))
fiction_department.add_item(Video("Війна і мир", 180, 1967, "Драма"))
fiction_department.add_item(Audio("Сонце", 4, 2021, "Анна", "MP3"))
fiction_department.add_item(Newspaper("Газета", "щоденна", "Видавництво", "Політика"))
fiction_department.add_item(Magazine("Журнал", "щомісячний", "Видавництво", "Україна"))

print(f"Усі матеріали відділу: {fiction_department.get_items()}")
fiction_department.remove_item("Лісова пісня")
print(f"Усі матеріали відділу після видалення: {fiction_department.get_items()}")
print(f"Відділ: {fiction_department}")

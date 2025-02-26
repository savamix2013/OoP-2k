import datetime

class Car:
    """змоделюємо машину"""


    def __init__(self, brand_or_car="Unknown", model="Unknown", year=0, mileage=0):
        """Опис машини який копіює в інший об'єкт Car"""
        current_year = datetime.datetime.now().year

        if isinstance(brand_or_car, Car):
            self.brand = brand_or_car.brand
            self.model = brand_or_car.model
            self.year = brand_or_car.year
            self.mileage = brand_or_car.mileage
        else: # Якщо передали звичайні значення
            self.brand = brand_or_car
            self.model = model
            if year > current_year:
                print(f"помилка: : рік випуску {year} не може бути більшим за {current_year}. Ставимо {current_year}.")
                self.year = current_year
            else:
                self.year = year
            self.mileage = mileage


    def __del__(self):
        """Видалення"""
        print("об'єкт знищено")


    def get_info(self):
        """Виводить інформацію про машину""" 
        return f"Марка: {self.brand}, модель: {self.model}, рік: {self.year}, пробіг: {self.mileage}."


    def update_mileage(self, new_mileage):
        """Змінює пробіг машини"""
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("Новий пробіг менше попереднього")


    def compare(self, other_car):
        """Порівнює два автомобілі за роком випуску та пробігом"""
        if self.year > other_car.year:
            print(f"{self.brand} {self.model} новіша за {other_car.brand} {other_car.model}.")
        elif self.year < other_car.year:
            print(f"{other_car.brand} {other_car.model} новіша за {self.brand} {self.model}.")
        else:
            if self.mileage > other_car.mileage:
                print(f"{other_car.brand} {other_car.model} має менший пробіг, ніж {self.brand} {self.model}.")
            elif self.mileage < other_car.mileage:
                print(f"{self.brand} {self.model} має менший пробіг, ніж {other_car.brand} {other_car.model}.")
            else:
                print(f"{self.brand} {self.model} і {other_car.brand} {other_car.model} однакові за віком і пробігом.")


car1 = Car("Toyota", "Camry", 2030, 50000)  # Тут має виправитися рік
print(car1.get_info()) 
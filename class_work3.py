import datetime

class Car:
    """змоделюємо машину"""


    def __init__(self, brand="Unknown", model="Unknown", year=0, mileage=0):
        """Опис машини"""
        current_year = datetime.datetime.now().year
        self.brand = brand
        self.model = model
        self.year = year if year <= current_year else current_year
        self.mileage = mileage

    def __del__(self):
        """Видалення"""
        print(f"Автомобіль {self.brand} {self.model} видалено з пам'яті.")

    def get_info(self):
        """Виводить інформацію про машину""" 
        return f"Марка: {self.brand}, модель: {self.model}, рік: {self.year}, пробіг: {self.mileage}."

    def copy(self):
        """Створює копію об'єкта"""
        return Car(self.brand, self.model, self.year, self.mileage)


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


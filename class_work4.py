from datetime import datetime

class Transport:
    def __init__(self, brand, model, year):
        self._brand = self._validate_string(brand, "Brand")
        self._model = self._validate_string(model, "Model")
        self._year = self._validate_year(year)

    def _validate_string(self, value, field_name):
        if not value.strip():
            raise ValueError(f"{field_name} не може бути порожнім!")
        return value

    def _validate_year(self, year):
        current_year = datetime.now().year
        if not (1900 <= year <= current_year):
            raise ValueError(f"Рік має бути в діапазоні 1900-{current_year}!")
        return year

    def get_info(self):
        return f"{self._brand} {self._model}, {self._year} рік"

    def __str__(self):
        return self.get_info()
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = self._validate_year(new_year)


class Car(Transport):
    def __init__(self, brand, model, year, passenger_count):
        Transport.__init__(self, brand, model, year)
        self._passenger_count = self._validate_passenger_count(passenger_count)
    
    def _validate_passenger_count(self, passenger_count):
        if passenger_count <= 0:
            raise ValueError("Кількість пасажирів має бути більше нуля!")
        return passenger_count

    def get_passenger_capacity(self):
        return self._passenger_count
    
    def move(self):
        return "Автомобіль їде по дорозі"

class Truck(Transport):
    def __init__(self, brand, model, year, cargo_capacity):
        Transport.__init__(self, brand, model, year)
        self._cargo_capacity = self._validate_cargo_capacity(cargo_capacity)
    
    def _validate_cargo_capacity(self, cargo_capacity):
        if cargo_capacity <= 0:
            raise ValueError("Вантажопідйомність має бути більше нуля!")
        return cargo_capacity

    def get_cargo_capacity(self):
        return self._cargo_capacity
    
    def move(self):
        return "Вантажівка перевозить вантаж"

class Bike(Transport):
    def __init__(self, brand, model, year, engine_volume):
        Transport.__init__(self, brand, model, year)
        self._engine_volume = self._validate_engine_volume(engine_volume)
    
    def _validate_engine_volume(self, engine_volume):
        if engine_volume <= 0:
            raise ValueError("Об'єм двигуна має бути більше нуля!")
        return engine_volume

    def get_engine_volume(self):
        return self._engine_volume
    
    def move(self):
        return "Мотоцикл мчить трасою"

if __name__ == "__main__":
    # Створюємо об'єкти
    car = Car("Toyota", "Corolla", 2020, 5)
    truck = Truck("Volvo", "FH", 2019, 20)
    bike = Bike("Yamaha", "YZF-R1", 2022, 998)

    # Додаємо їх до списку
    vehicles = [car, truck, bike]

    # Виводимо інформацію та метод move()
    for vehicle in vehicles:
        print(vehicle.get_info())  # Викликаємо get_info()
        print(vehicle.move())  # Викликаємо move()
        
        # Перевірка типу транспортного засобу
        if isinstance(vehicle, Car):
            print(f"Кількість пасажирів: {vehicle.get_passenger_capacity()}")
        elif isinstance(vehicle, Truck):
            print(f"Вантажопідйомність: {vehicle.get_cargo_capacity()} тонн")
        elif isinstance(vehicle, Bike):
            print(f"Об'єм двигуна: {vehicle.get_engine_volume()} куб. см")

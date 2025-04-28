from abc import ABC, abstractmethod

# Інтерфейс Observer
class Observer(ABC):
    @abstractmethod
    def update(self, stock_name: str, new_price: float):
        pass

# Інтерфейс Subject
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Клас StockExchange (біржа)
class StockExchange(Subject):
    def __init__(self):
        self.observers = []
        self.stock_name = ""
        self.stock_price = 0.0

    def set_stock_price(self, stock_name: str, new_price: float):
        self.stock_name = stock_name
        self.stock_price = new_price
        self.notify_observers()

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.stock_name, self.stock_price)

# Клас Investor (інвестор)
class Investor(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, stock_name: str, new_price: float):
        print(f"Інвестор {self.name} повідомлений: Акція {stock_name} змінила ціну на {new_price}")

# Клас Broker (брокер)
class Broker(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, stock_name: str, new_price: float):
        print(f"Брокер {self.name} повідомлений: Акція {stock_name} тепер коштує {new_price}")

# Тестування
if __name__ == "__main__":
    # Створення біржі
    stock_exchange = StockExchange()

    # Створення підписників
    investor1 = Investor("Олександр")
    investor2 = Investor("Марія")
    broker = Broker("Компанія 'ТрейдМакс'")

    # Додаємо підписників
    stock_exchange.attach(investor1)
    stock_exchange.attach(investor2)
    stock_exchange.attach(broker)

    # Зміна курсу акцій
    stock_exchange.set_stock_price("Apple", 145.50)
    stock_exchange.set_stock_price("Google", 2730.20)

    # Видалення одного підписника
    stock_exchange.detach(investor2)

    # Зміна курсу акцій
    stock_exchange.set_stock_price("Microsoft", 310.00)

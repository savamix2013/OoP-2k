from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total


class VolumeDiscount(DiscountStrategy):
    def apply_discount(self, total):
        if total > 200:
            return total * 0.9  # 10% знижка
        return total


class OrderManager:
    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    def add_item(self, item_name, quantity):
        if item_name in self.menu:
            self.order[item_name] = self.order.get(item_name, 0) + quantity
        else:
            print("Страва не знайдена в меню.")

    def calculate_total(self):
        return sum(self.menu[item] * quantity for item, quantity in self.order.items())


class ReceiptGenerator:
    def generate(self, order, total):
        print("\nЧек:")
        for item, quantity in order.items():
            print(f"{item} x{quantity} = {menu[item] * quantity} грн")
        print(f"Загальна сума: {total:.2f} грн")


class CafeSystem:
    def __init__(self, order_manager, discount_strategy, receipt_generator):
        self.order_manager = order_manager
        self.discount_strategy = discount_strategy
        self.receipt_generator = receipt_generator

    def process_order(self):
        total = self.order_manager.calculate_total()
        discounted_total = self.discount_strategy.apply_discount(total)
        self.receipt_generator.generate(self.order_manager.order, discounted_total)

# --- Використання ---
menu = {
    "Кава": 50,
    "Чай": 40,
    "Тістечко": 60
}

order_manager = OrderManager(menu)
discount_strategy = VolumeDiscount()  # Можна замінити на іншу стратегію
receipt_generator = ReceiptGenerator()

system = CafeSystem(order_manager, discount_strategy, receipt_generator)

order_manager.add_item("Кава", 3)
order_manager.add_item("Тістечко", 2)
system.process_order()

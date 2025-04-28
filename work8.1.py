class CafeOrder:
    def __init__(self):
        self.menu = {
            "Кава": 50,
            "Чай": 40,
            "Тістечко": 60
        }
        self.order = {}
        self.total = 0

    def add_item(self, item_name, quantity):
        if item_name in self.menu:
            self.order[item_name] = self.order.get(item_name, 0) + quantity
        else:
            print("Страва не знайдена в меню.")

    def calculate_total(self):
        self.total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        self.apply_discount()

    def apply_discount(self):
        # Фіксована знижка 10% при сумі більше 200
        if self.total > 200:
            self.total *= 0.9

    def generate_receipt(self):
        print("\nЧек:")
        for item, quantity in self.order.items():
            print(f"{item} x{quantity} = {self.menu[item] * quantity} грн")
        print(f"Загальна сума: {self.total:.2f} грн")

# Використання
order = CafeOrder()
order.add_item("Кава", 3)
order.add_item("Тістечко", 2)
order.calculate_total()
order.generate_receipt()

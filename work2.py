import random

class BankAccount:

    account_current = 1000000000

    """функції рахунку клієнта"""
    def __init__(self, account_number, owner_name, balance):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.set_balance(balance)

    def generate_account_number():
        """Статичний метод для генерування унікального номера рахунку"""
        return str(random.randint(1000000000, 9999999999))


    def get_account_info(self):
        """Геттер"""
        return f"Account number: {self.__account_number}, Owner name: {self.__owner_name}"


    def set_owner_name(self, new_name):
        """Сеттер"""
        if len(new_name) >= 3:
            self.__owner_name = new_name
        else:
            print("Помилка: Ім'я має містити принаймні 3 символи.")

    
    def set_balance(self, amount):
        """Сетер для балансу з перевіркою на від'ємне значення"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Помилка: Баланс не може бути від'ємним.")  


    def deposit(self, amount):
        """Метод для внесення коштів"""
        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount}. Новий баланс: {self.__balance}.")
        else:
            print("Помилка: Некоректна сума для внесення коштів.")


    def withdraw(self, amount):
        """Зняття коштів"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято: {amount}. Новий баланс: {self.__balance}.")
        else:
            print("Помилка: Некоректна сума для зняття коштів.")


    def get_balance(self):
        return self.__balance
    

# account = BankAccount("UA132456789", "Всеволод", 1000)
# print(account.get_account_info())
# account.set_owner_name("ma")
# account.deposit(500)
# account.withdraw(200)
# print(f"Balance {account.get_balance()} ")
# print(account.get_account_info())

account1 = BankAccount(BankAccount.generate_account_number(), "Всеволод", 1000)
print(account1.get_account_info())  # Виведе унікальний номер рахунку
getbalance = account1.get_balance()
print(getbalance)


account2 = BankAccount(BankAccount.generate_account_number(), "Ірина", 500)
print(account2.get_account_info())  # Виведе новий унікальний номер рахунку
getbalance = account2.get_balance()
print(getbalance)


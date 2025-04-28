from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def add(self, employee):
        pass

    @abstractmethod
    def remove(self, employee):
        pass

    @abstractmethod
    def get_subordinates(self):
        pass

    @abstractmethod
    def display_info(self, indent=0):
        pass


class IndividualEmployee(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def add(self, employee):
        print(f"Не можна додати підлеглого до {self.name}, оскільки це окремий співробітник.")

    def remove(self, employee):
        print(f"Немає підлеглих для видалення у {self.name}.")

    def get_subordinates(self):
        return []

    def display_info(self, indent=0):
        print(" " * indent + f"{self.position}: {self.name}")


class Department(Employee):
    def __init__(self, name, position="Head of Department"):
        self.name = name
        self.position = position
        self.subordinates = []

    def add(self, employee):
        self.subordinates.append(employee)

    def remove(self, employee):
        self.subordinates.remove(employee)

    def get_subordinates(self):
        return self.subordinates

    def display_info(self, indent=0):
        print(" " * indent + f"{self.position}: {self.name}")
        for subordinate in self.subordinates:
            subordinate.display_info(indent + 4)

    def count_employees(self):
        count = 0
        for subordinate in self.subordinates:
            if isinstance(subordinate, Department):
                count += subordinate.count_employees()
            else:
                count += 1
        return count

    def find_employee(self, name):
        for subordinate in self.subordinates:
            if isinstance(subordinate, IndividualEmployee) and subordinate.name == name:
                return subordinate
            elif isinstance(subordinate, Department):
                found = subordinate.find_employee(name)
                if found:
                    return found
        return None



# Створюємо співробітників
emp1 = IndividualEmployee("Іван Петренко", "Розробник")
emp2 = IndividualEmployee("Олена Коваль", "Тестувальник")
emp3 = IndividualEmployee("Марія Іванова", "HR")

# Створюємо відділи
dev_department = Department("Відділ розробки")
qa_department = Department("Відділ тестування")
hr_department = Department("HR-відділ")

# Додаємо співробітників до відділів
dev_department.add(emp1)
qa_department.add(emp2)
hr_department.add(emp3)

# Створюємо головний департамент
head_office = Department("Головний офіс", "CEO")
head_office.add(dev_department)
head_office.add(qa_department)
head_office.add(hr_department)

# Відображення всієї структури
head_office.display_info()

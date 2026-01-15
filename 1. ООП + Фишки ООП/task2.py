class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return 'succes'


class Developer(Employee):
    def __init__(self, programming_language, name, position, salary):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        return 'info dev'


class Manager(Employee):
    def __init__(self,employees, name, position, salary):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        return 'info list'


a = Developer('Python','Anton', 'middle', 150)
b = Manager('[тут должен быть список]', 'Kostya', 'senior', '$5000' )
c = Employee('Tema', 'jun', 50)

print(a.get_info())
print(b.get_info())
print(c.get_info())



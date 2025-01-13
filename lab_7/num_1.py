class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя: {self.name}, ID: {self.id}'


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        print(f'Менеджер {self.name} управляет проектом в отделе {self.department}.')


class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f'Техник {self.name} выполняет техническое обслуживание как {self.specialization}.')


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        self.specialization = specialization
        self.sot = list()

    def add_employee(self, employee):
        self.sot.append(employee.get_info())

    def get_team_info(self):
        return f'Состав команды:{self.sot}'

    def manage_projects(self):
        print(f'Технический менеджер {self.name} управляет проектами в отделе {self.department}.')

    def perform_maintenances(self):
        print(f'Технический менеджер {self.name} выполняет техническое обслуживание как {self.specialization}.')


Zhenya = Employee('Евгений Творожкин', '1')
Volodya = Manager('Володя Шарапов', '2', 'IT')
Serega = Technician('Серега Пират','3', 'Мега крутой специалист')

David = TechManager('Давид Тагиров', '4', 'Связь', 'обновлятор ПО')


Volodya.manage_project()
Serega.perform_maintenance()

David.add_employee(Zhenya)
David.add_employee(Volodya)
David.add_employee(Serega)

print(David.get_team_info())

David.manage_projects()
David.perform_maintenances()
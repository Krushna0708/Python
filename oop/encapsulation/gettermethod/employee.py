class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

e1 = Employee()
print(e1.get_salary())
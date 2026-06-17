class Employee:
    def __init__(self):
        self.__salary = 50000
    def set_salary(self, sal):
        self.__salary = sal

    def get_salary(self):
        return self.__salary

e1 = Employee()
e1.set_salary(60000)
print(e1.get_salary())
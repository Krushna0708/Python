class Employee:
    def __init__(self):
        self.__salary = 50000

    @property
    def s_salary(self):
        return self.__salary

e1 = Employee()
print(e1.s_salary)
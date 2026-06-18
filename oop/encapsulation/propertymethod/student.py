class Student:
    def __init__(self):
        self.__marks = 55

    @property
    def show(self):
        return self.__marks

m1 = Student()
print(m1.show)
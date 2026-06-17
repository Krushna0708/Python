class Student:
    def __init__(self):
        self.__marks = 95

    def get_marks(self):
        return self.__marks

s1 = Student()
print(s1.get_marks())
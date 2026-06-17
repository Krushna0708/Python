class Student:
    def __init__(self):
        self.__marks = 50

    def set_marks(self , m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s1 = Student()
s1.set_marks(90)
print(s1.get_marks())
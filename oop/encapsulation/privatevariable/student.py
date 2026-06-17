class Student :
    def __init__(self):
        self.__marks = 95

    # Using A getter method because private variable
    # are not directly accessible outside the class

    def get_marks(self):
        return self.__marks

m1 = Student()
print(m1.get_marks())
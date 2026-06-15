class Person:
    def __init__(self):
        print("Person Created")

class Student(Person):
    pass

class Teacher(Person):
    pass

s1 = Student()
t1 = Teacher()
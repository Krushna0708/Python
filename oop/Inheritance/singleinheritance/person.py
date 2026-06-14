# single inheritance practice problem

class Person:
    def walk(self):
        print("Walking")

class Student(Person):
    def study(self):
        print("Studying")

s1 = Student()
s1.walk()
s1.study()
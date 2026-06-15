class Person:
    def walk(self):
        print("Walking")

class Student(Person):
    def study(self):
        print("Studying")

class Teacher(Person):
    def tech(self):
        print("Teaching")

s1 = Student()
s1.walk()
s1.study()

print("-------------")

t1 = Teacher()
t1.walk()
t1.tech()
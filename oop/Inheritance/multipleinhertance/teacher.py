class Teacher:
    def teach(self):
        print("Teacher")

class Coder:
    def code(self):
        print("Coding")

class Student(Teacher,Coder):
    def study(self):
        print("Studying")

s1 = Student()
s1.teach()
s1.code()
s1.study()
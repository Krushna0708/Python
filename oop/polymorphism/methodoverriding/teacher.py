class Teacher:
    def work(self):
        print("Teaching")

class Student(Teacher):
    def work(self):
        print("Studying")

s1 = Student()
s1.work()
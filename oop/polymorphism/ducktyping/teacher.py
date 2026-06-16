class Teacher:
    def work(self):
        print("Teaching")

class Student:
    def work(self):
        print("Studying")

def display(obj):
    obj.work()

t1 = Teacher()
s1 =  Student()

display(t1)
display(s1)
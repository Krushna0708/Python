class Person:
    def intro(self):
        print("I am Person")

class Student:
    def intro(self):
        print("I am Student")

def do_intro(obj):
    obj.intro()

p1 = Person()
s1 = Student()

do_intro(p1)
do_intro(s1)
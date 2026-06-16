class Employee:
    def work(self):
        print("Work in Company")

class Developer:
    def work(self):
        print("Code")

def display(obj):
    obj.work()

e1 = Employee()
d1 = Developer()

display(e1)
display(d1)
class Employee:
    def work(self):
        print("Working in Company")

class Developer(Employee):
    def work(self):
        super().work()
        print("Coding")

d1 = Developer()
d1.work()
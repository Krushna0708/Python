class Laptop:
    def show(self):
        print("Laptop Start")

class Mobile:
    def show(self):
        print("Mobile Start")

def display(obj):
    obj.show()

l1 = Laptop()
m1 = Mobile()

display(l1)
display(m1)
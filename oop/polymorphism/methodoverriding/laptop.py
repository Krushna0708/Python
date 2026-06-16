class Mobile:
    def show(self):
        print("Mobile")

class Laptop(Mobile):
    def show(self):
        print("Laptop")

l1 = Laptop()
l1.show()
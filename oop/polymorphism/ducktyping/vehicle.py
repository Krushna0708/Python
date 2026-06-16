class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car:
    def start(self):
        print("Car Started")

def make_start(b1):
    b1.start()

v1 = Vehicle()
c1 = Car()

make_start(v1)
make_start(c1)
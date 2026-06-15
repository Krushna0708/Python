class Vehicle:
    def start(self):
        print("Started")

class Car(Vehicle):
    def drive(self):
        print("Driving")

class Bike(Vehicle):
    def ride(self):
        print("Riding")

c1 = Car()
c1.start()
c1.drive()

print("------------------")

b1 = Bike()
b1.start()
b1.ride()
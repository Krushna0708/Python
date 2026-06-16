class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car Started")

c1 = Car()
c1.start()
# create parent class vehicle, child class Car
# and method start() create object and call start() method and print "Vehicle Started"

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

c1 = Car()
c1.start()

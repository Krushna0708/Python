class Grandfather:
    def land(self):
        print("Land")

class Father(Grandfather):
    def house(self):
        print("House")

class Son(Father):
    def bike(self):
        print("Bike")

s1 = Son()
s1.land()
s1.house()
s1.bike()
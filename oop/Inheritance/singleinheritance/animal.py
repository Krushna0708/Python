# create parent class animal, child class Dog
# and method eat() create object and call eat() method and print "EATING"

class Animal:
    def eat(self):
        print("EATING")

class Dog(Animal):
    pass

d1 = Dog()
d1.eat()
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meow")

d1 = Dog()
d1.eat()
d1.bark()

print("-----------------")

c1 =  Cat()
c1.eat()
c1.meow()
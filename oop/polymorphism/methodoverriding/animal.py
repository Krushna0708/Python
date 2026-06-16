class Animal:
    def sound(self):
        print("ANimal Sound")

class Dog(Animal):
    def sound(self):
        print("Baring")

d1 = Dog()
d1.sound()

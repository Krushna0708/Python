class Dog:
    def sound(self):
        print("Barking")

class Cat(Dog):
    def sound(self):
        print("Meow")

c1 = Cat()
c1.sound()
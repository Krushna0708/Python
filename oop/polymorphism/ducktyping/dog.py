class Dog:
    def sound(self):
        print("Barking")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(obj):
    obj.sound()

d1 = Dog()
c1 = Cat()

make_sound(d1)
make_sound(c1)
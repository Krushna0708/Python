class Animal:
    def eat(self):
        print('Eating')

class Dog(Animal):
    def Bark(self):
        print("Barking")

class Puppy(Dog):
    def sleep(self):
        print("Sleeping")

p1 = Puppy()
p1.eat()
p1.Bark()
p1.sleep()
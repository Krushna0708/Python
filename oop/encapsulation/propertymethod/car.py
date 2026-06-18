class Car:
    def __init__(self):
        self.__speed = 120

    @property
    def show(self):
        return self.__speed 

c1 = Car()
print(c1.show)
class Car:
    def __init__(self):
        self.__speed = 120

    def get_speed(self):
        return self.__speed

c1 = Car()
print(c1.get_speed())
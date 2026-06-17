class Car:
    def __init__(self):
        self.__speed = 120

    def set_speed(self , s):
        self.__speed = s

    def get_speed(self):
        return self.__speed

c1 = Car()
c1.set_speed(150)
print(c1.get_speed())
class Mobile:
    def __init__(self):
        self.__price = 20000

    @property
    def show(self):
        return self.__price

m1 = Mobile()
print(m1.show)
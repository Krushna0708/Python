class Mobile:
    def __init__(self):
        self.__price = 20000

    def get_price(self):
        return self.__price

m1 = Mobile()
print(m1.get_price())
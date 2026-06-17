class Mobile:
    def __int__(self):
        self.__price = 20000

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

m1 = Mobile()
m1.set_price(25000)
print(m1.get_price())
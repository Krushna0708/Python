class Mobile:
    def __init__(self):
        self.__price = 20000          # private variable

    def set_price(self,amount):
        self.__price = amount         # Setter method

    def get_price(self):              # Getter method
        return self.__price

m1 = Mobile()
m1.set_price(25000)
print(m1.get_price())
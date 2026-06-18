class Bank:
    def __init__(self):
        self.__balance = 130000

    @property
    def balance(self):
        return self.__balance

b1 = Bank()
print(b1.balance)
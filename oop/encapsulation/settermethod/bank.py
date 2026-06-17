class Bank:
    def __init__(self):
        self.__balance = 120000

    def set_balance(self , balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

b1 = Bank()
b1.set_balance(150000)
print(b1.get_balance())
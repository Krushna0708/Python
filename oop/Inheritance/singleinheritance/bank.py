class Bank:
    def bank_name(self):
        print("SBI")

class Customer(Bank):
    def customer_name(self):
        print("Krushna")

c1 = Customer()
c1.bank_name()
c1.customer_name()
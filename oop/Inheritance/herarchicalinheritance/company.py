class Company:
    def company_name(self):
        print("TCS")

class Developer(Company):
    def code(self):
        print("Coding")

class Tester(Company):
    def test(self):
        print("Testing")

d1 = Developer()
d1.code()
d1.company_name()

t1 = Tester()
t1.test()
t1.company_name()
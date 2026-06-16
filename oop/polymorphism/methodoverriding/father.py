class Father:
    def work(self):
        print("Working")

class Son(Father):
    def work(self):
        print('Studying')

f1 = Father()
f1.work()
s1 = Son()
s1.work()
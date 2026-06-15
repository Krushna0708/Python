class Father:
    def money(self):
        print("Money")

class Mother:
    def care(self):
        print("Care")

class Son(Father,Mother):
    def study(self):
        print("Studying")

s1 = Son()
s1.money()
s1.care()
s1.study()
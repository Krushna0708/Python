# Constructor With Method

class Main:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(self.name)

m1 = Main("Krushna")
m1.greet()

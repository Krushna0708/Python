class Samsung:
    def call(self):
        print("Samsung Calling")

class Apple(Samsung):
    def call(self):
        print("Apple Calling")

a1 = Apple()
a1.call()
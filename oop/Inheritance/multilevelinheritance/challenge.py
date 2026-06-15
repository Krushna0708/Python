class Grandfather:
    def __init__(self):
        print("Land")

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        print("House")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Bike")

s1 = Son()
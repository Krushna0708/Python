class Father:
    def __init__(self):
        print("Money")
        super().__init__()

class Mother:
    def  __init__(self):
        print("Care")
        super().__init__()

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Studying")

s1 = Son()


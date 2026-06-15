class A:
    def __init__(self):
        print("A")
        super().__init__()

class B:
    def __init__(self):
        print("B")
        super().__init__()

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C")
    

c1 = C()
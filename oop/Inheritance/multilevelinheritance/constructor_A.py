class A:
    def __init__(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

c1 = C()

class A:
    def show(self):
        print("A")

class B(A):
    pass
class c(B):
    pass

c1 = c()
c1.show()
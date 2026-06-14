class Mobile:
    def __init__(self):
        print("Samsung")

class SmartPhone(Mobile):
    def __init__(self):
        super().__init__()
        print("Galaxy")

s1 = SmartPhone()
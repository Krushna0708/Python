class Singer:
    def sing(self):
        print("Singing")

class Dancer:
    def dance(self):
        print("Dancing")

class Artist(Singer,Dancer):
    def draw(self):
        print("Drawing")

a1 = Artist()
a1.sing()
a1.dance()
a1.draw()
# Encapsulation Public Access Specifier Problem

class Student:
    def __init__(self):
        self.name = "Krushna"

s = Student()
print(s.name)
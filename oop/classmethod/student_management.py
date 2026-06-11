class Student :
    school = "ABC School"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("Name :",self.name)
        print("Age :",self.age)

    @classmethod
    def show_school(cls):
        print("School :",cls.school)
        print("-----------------")


s1 = Student("Krushna",20)
s2 = Student("Rahul",25)

s1.show()
Student.show_school()

s2.show()
Student.show_school()
        
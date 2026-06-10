class Student:
    Collage = "ABC Collage"
    def __init__(self,name,age,batch):
        self.name = name 
        self.age = age 
        self.batch = batch

    def greet(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Batch :",self.batch)
        print("Collage :",self.Collage)
        print("--------------------------------------")

s1 = Student("Krushna",20,"AIML")
s2 =Student("Rahul",19,"CSE")
s3 =Student("Deepak",21,"IT")

s1.greet()
s2.greet()
s3.greet()
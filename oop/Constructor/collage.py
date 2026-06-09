# Program with multiple Objects And Parameters

class Collage:
    def __init__(self,name,age,branch,course):
        self.name = name
        self.age = age
        self.branch = branch
        self.course = course

s1 = Collage("Krushna",20,"AIML","BTech")
s2 = Collage("Akash",21,"CSE","BTech")

print(s1.name,"\n",s1.age,"\n",s1.branch,"\n",s1.course)
print(s2.name,"\n",s2.age,"\n",s2.branch,"\n",s2.course)
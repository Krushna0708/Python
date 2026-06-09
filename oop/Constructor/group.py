class Group:
    def __init__(self,name,age,batch,marks,percentage,hobbies,course):
        self.name =name
        self.age = age
        self.batch =batch
        self.marks = marks
        self.percentage = percentage
        self. hobbies = hobbies
        self.course = course

g1 = Group("Krushna",20,"AIML",76,75.9, "Coding","Btech")
g2 = Group("Rahul",30,"AI",70,69.9, "Reading","Btech")
g3 = Group("Pooja",25,"ML",65,60.9, "Boxing","Btech")


print(g1.name,g1.age,g1.batch,g1.marks,g1.percentage,g1.hobbies,g1.course)
print(g2.name,g2.age,g2.batch,g2.marks,g2.percentage,g2.hobbies,g2.course)
print(g3.name,g3.age,g3.batch,g3.marks,g3.percentage,g3.hobbies,g3.course)

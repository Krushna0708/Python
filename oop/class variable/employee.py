class Employee:
    Company = "Google"
    def __init__(self,name,age,role,salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

    def greet(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Role :",self.role)
        print("Salary :",self.salary)
        print("Company :",self.Company)
        print("--------------------------------------------------------------------------")

e1 = Employee("Krushna",20,"AI Engineer",270000)
e2 = Employee("Rahul",30,"WEB Developer",180000)
e3 = Employee("Deepak",28,"Software Developer",230000)

e1.greet()
e2.greet()
e3.greet()
class Employee:
    company = "Infosys"
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def show(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        print("Role :",self.role)
    @classmethod
    def show_company(cls):
        print("Company :",cls.company)
        print("=======================")

e1 = Employee("Krushna",280000,"AI Engineer")
e2 = Employee("Rahul",180000,"Web Developer")
e3 = Employee("Deepak",250000,"Software Engineer")

e1.show()
Employee.show_company()
e2.show()
Employee.show_company()
e3.show()
Employee.show_company()


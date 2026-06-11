class Employee:
    company = "Infosys"
    def __init__(self,name):
        self.name = name

    def show(self):
        print("Name :",self.name)
    @classmethod
    def show_company(cls):
        print("Company :",cls.company)

e1 = Employee("Krushna")
e1.show()
e1.show_company()
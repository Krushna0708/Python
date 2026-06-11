class Employee:
    company = "Infosys"
    @classmethod
    def show(cls):
        cls.company = "Google"
        print("Company :",cls.company)
e1 = Employee()
e1.show()
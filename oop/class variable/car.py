class Car:
    showroom = "AJIKYA KIA"
    def __init__(self,car_name,Model,Price):
        self.car_name = car_name
        self.Model = Model
        self.Price = Price

    def greet(self):
        print("Car_name :",self.car_name)
        print("Car Model :",self.Model) 
        print("Car Price :",self.Price)
        print("Showroom Name :",self.showroom)
        print("---------------------------------------------------")

c1 = Car("KIA",2026,2500000)
c2 = Car("TATA Punch",2025,2300000)
c3 = Car("Thar_Rox",2026,2500000)

c1.greet()
c2.greet()
c3.greet()
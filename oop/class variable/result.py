class Student:
    School = "ABC School"
    def __init__(self,student_name,math,science,english,marathi,hindi,social_science):
        self.student_name = student_name
        self.math = math
        self.science = science
        self.english = english
        self.marathi = marathi
        self.hindi = hindi
        self.social_science = social_science

    def greet(self):
        print("Student Name :",self.student_name)
        print("School Name :",self.School)
        print("-----------Result ------------")
        print("Math :"         ,self.math)
        print("Science :"       ,self.science)
        print("English :"       ,self.english)
        print('Marathi:'        ,self.marathi)
        print("Hindi :"         ,self.hindi)
        print("Social Science :",self.social_science)
        print("----------------------------------------------------------------------")
        total_marks = self.math + self.science + self.english + self.marathi + self.hindi + self.social_science
        print("Total Marks :",total_marks)

        percentage = total_marks / 600 *100
        print("Percentage :",percentage)
        print("========================================================================")

s1 = Student("Krushna",86,75,92,97,96,77)
s2 = Student("Rahul",76,81,88,89,95,78)
s3 = Student("Deepak",88,78,85,89,91,75)

s1.greet()
s2.greet()
s3.greet()

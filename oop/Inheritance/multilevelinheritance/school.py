class School:
    def school_name(self):
        print("ABC School")

class Teacher(School):
    def teacher_name(self):
        print("Niraj")

class Student(Teacher):
    def student_name(self):
        print("Krushan")

s1 = Student()
s1.school_name()
s1.teacher_name()
s1.student_name()
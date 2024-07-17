class Student:
    school_name = "Aravinda"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def details(self):
        print(f"{self.name}, {self.roll_no}, {self.school_name}")
        self.school_name = "SJCIT"


student_1 = Student("Manju", 55)
student_1.details()
student_1.details()

student_1 = Student("Ram", 1)
student_1.details()
"""
- data and methods together is called blueprint or class 
- a variable that stores the data about a class is called object 
- that object is an instance of a class 


class student:
    name = ""
    DOB = "" 
    program = "" 
    mark = 0 
    def FindAge():
        print(DOB)
    def Grade(mark):
        if mark >= 40:
            print("pass")
        else:
            print("fail")


print(student)
#std1 = student("ali", "5 sep 2015", "AI and data science", 90)
std1 = student()
print(std1)
std1.name = "ali"
print(std1.name)
std1.DOB = "5sep2010"
std1.program = "aianddatascience"
std1.mark = 90
print("student name : ", std1.name)
print("student DOB : ", std1.DOB)
print("student program : ", std1.program)
print("student total mark : ", std1.mark)
std1.Grade(std1.mark)


std2 = student()
std2.name = "amal"
std2.DOB = "10sep2010"
std2.program = "cyber"
std2.mark = 88
print("student name : ", std2.name)
print("student DOB : ", std2.DOB)
print("student program : ", std2.program)
print("student total mark : ", std2.mark)

"""

class student():
    def __init__(self, name, DOB , program, mark):
        self.name = name 
        self.DOB = DOB 
        self.program = program 
        self.mark = mark 

    def findAge(self):
        print(self.DOB)
    def grade(self):
        if self.mark >= 40:
            print("pass")
        else:
            print("fail")

std1 = student("ali", "5 sep 2015", "AI and data science", 90)
std2 = student("babar", "12 feb 2008", "IT", 34)

std1.findAge()
std1.grade()

std2.findAge()
std2.grade()


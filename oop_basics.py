#class with variables
class Student:
    name="Durga"
    age= 20
s1=Student()
print(s1.name)
print(s1.age)

#constructor(__init__)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Durga",20)
s2=Student("Bhavani",19)
print(s1.name,s1.age)
print(s2.name,s2.age)

#Methods(Functions inside class)
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name",self.name)
        print("Marks",self.marks)
s1 =Student("Durga",99)
s1.display()

#mini project: Student Info System
class Student:
    def __init__(self,name,roll): 
        self.name=name
        self.roll=roll
    def show(self):
        print("Name",self.name)
        print("Roll No",self.roll)
s1=Student("durga",101)
s1.show()
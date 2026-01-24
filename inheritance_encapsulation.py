#inheritance
    #one class inherits properties of another class
#Example(parent -> child)
"""
class Parent:
    def house(self):
        print("This is a house")
class Child(Parent):
     def car(self):
        print("This is a car")
c = Child()
c.house()
c.car() 
"""
#inheritance with constructor
class person:
    def __init__(self,name):
        self.name = name
class Student(person):
    def show(self):
        print("Name:",self.name)
s=Student("Durga")
s.show()
#Example (Multilevel Inheritance)
class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
class C(B):
    def showC(self):
        print("C")
obj = C()
obj.showA()
obj.showB()
obj.showC()

#Encapsulation
class Bank:
    def __init__(self):
        self.__balance = 1000 #private variable
    def show_balance(self):
        print("Balance:",self.__balance)
    def deposit(self,amount):
        self.__balance += amount
b = Bank()
b.show_balance()
b.deposit(500)
b.show_balance()

        #why encapsulation?
        #to protect data from unauthorized access
        #to achieve data hiding
#MINI Project: Bank Account
class Account:
    def __init__(self):
        self.__balance = 0
    def deposit(self,amt):
        self.__balance += amt
    def withdraw(self,amt):
        if amt <= self.__balance:
            self.__balance-=amt
        else:
            print("Insufficient balance")
    def show(self):  
            print("Balance:",self.__balance) 
a=Account()
a.deposit(1000)
a.withdraw(500)
a.show()    
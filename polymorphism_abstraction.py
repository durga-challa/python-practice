'''class Dog:                   #Same methodname in different classes
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
for animal in (Dog(), Cat()):
    animal.sound()
    '''
    #funtions in polymorphism
'''
print(len("Durga"))
print(len([1,2,3,4,]))
'''

#Abstraction
#Show only what is needed and hide the details

#Child Class Implimentation
'''
class Rectangle:
    def area(self):
        print("Area = length*breadth")
r = Rectangle()
r.area()
'''

#MINI PROJECT (OOP)
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        print("Area = side*side")
class Circle(Shape):
    def area(self):
        print("Area = 3.14*r*r")
s = Square()
c = Circle()
s.area()
c.area()
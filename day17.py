'''
Inheritance:
-->This allows one class to aquire the properties and methods of another class ...
Types of Inheritence
1.Single Inheritance
--------------------
-->A class inherits from  a single parent class...     
Eg:
class father:
    def land(self):
        print("My Father have 5acars")

class purni(father):
    def my_own(self):
        print(" I have 2 acers")

hai=purni()
hai.land()
Output:
My Father have 5acars

2.Multipule Inheritance
-----------------------
-->A child class inherits from more than one parent class...
Eg:
class father:
    def land(self):
        print("My Father have 5acars")
class mother:
    def gold(self):
        print("My mother have 1kg gold")
class son(father,mother):
    def mine(self):
        print(" I have ntg")
hai=son()
hai.land()
hai.gold()
Output:
My Father have 5acars
My mother have 1kg gold

3.Multilevel Inheritance:(no need to mention the grand father in son class)
-------------------------
-->A class inheries from a parent class and another class inherits from that child class.
EG:
class grandfather:
    def land(self):
        print("My grandFather have 5acars of land")
class father(grandfather):
    def flat(self):
        print("My father have flatat BNG")
class son(father):
    def ntg(self):
        print("I wont both of their properties")
hai=son()
hai.land()
hai.flat()
hai.ntg()
Output:
My grandFather have 5acars of land
My father have flatat BNG
I wont both of their properties
4.Hierarical Inheritance:
-------------------------
-->Multiple child classes inherits from a single parent..
class father:
    def land(self):
        print("10 cares land")

class purni(father):
    def mine(self):
        print("job")

class hyma(father):
    def sis(self):
        print("jobless")

d1=hyma()
d1.land()

d2=purni()
d2.land()
Output:
10 cares land
10 cares land

5.Hybride Inheritance
---------------------
--> This is the combination of two or more inheritance 
Eg:
class A:
    def some(self):
        print('class A')
class B(A):
    def any(self):
        print('class B')
class C(A):
    def so(self):
        print('class C')
class D(B,C):
    def ALL_(self):
        print('class D')
hai=D()
hai.so()
hai.some()
hai.any()
hai.ALL_()

Output:
class C
class A
class B
class D

---------


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()   
c.drive()
Output:
Vehicle is starting
Car is driving

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()
d.bark()
Output:
Animal is eating
Dog is barking

class Device:
    def power_on(self):
        print("Device powered on")

class Laptop(Device):
    def code(self):
        print("Coding on laptop")

l = Laptop()
l.power_on()
l.code()
Output:
Device powered on
Coding on laptop


Super()method:
-------------
-->super() is used to access methods and constructors of the parent class from the child class.
EG:
class parent:
    def display(self):
        print('Method Parent')
class child(parent):
    def display(self):
        super().display()
        print('Method Child')

any_=child()
any_.display()
Output:
Method Parent
Method Child

'''
class person:
    def __init__(self,name):
        self.name =name
class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll =roll
    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        
hai=stu_('poornima',179)
hai.show()
Output:
Name: poornima
Roll No: 179
        
        







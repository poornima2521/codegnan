'''
OOPS:
----
1.Class:
--------
--> A class is a blueprint or template is used to creat object.
-->eg:
    class stu_:
    name='poornima'

2.Object:
-->An object is an instance of a class.
Eg
--
class stu_:
    name='poornima'
s1=stu_()
print(s1.name)
Output:
poornima

class stu_:
    def edu_(self):
        print("I am studying bsc")
    def sports_(self):
        print("cricket")
        print("vallyboll")
s1=stu_()
s1.edu_()
s1.sports_()
Output:
I am studying bsc
cricket
vallyboll
3.Attribute:
------------
-->Attributes or the variables that belongs to a class or an object.
--> variables in side the class or object.
Eg
---
class stu_:
    name='poornima'
    age=20
s1=stu_()
print(s1.name)
print(s1.age)

Output:
poornima
20

4.Methods:
----------
-->The functions defined inside the class in methods.
Eg:
class PFS_DA:
    def python(self):
        PFS_DA='Batch_03'
        print('This is PFS and DA batch03')

    def Flask(self):
        PFS='Batch_03'
        print('This is PFS batch03')
all_=PFS_DA()
all_.python()
all_.Flask()
5.Constructor  (__init__)
-------------
-->constructor is a special method that is automatically called when an object is created. 
Eg
--
class ATM:
    def __init__(self,Balance,name):
        self.Balance = Balance
        self.name = name

    def Bal_check(self):
        print(f"{self.name} your total balance is {self.Balance+700}")

    def name_(self):
        print(self.name)
        
card=ATM(Balance =50000,name='Poornima')
card.Bal_check()
card.name_()
        
Output:
Poornima your total balance is 50700
Poornima

#Access Specifiers
------------------
1.Public
--------
-->This can be accessed feom anywherein the program
Eg
--

2.Protected(_balance)
---------------------
-->This is representing using single underscore(_)
Eg:

class stu_:
    _name='poornima'
s1 = stu_()
print(s1._name)
Output:
poornima

3.private(__balance)
--------------------
-->This is represented using a double underscore(__)
class stu:
    __name='poornima'
s1= stu()
print(s1._stu__name)
Output:
poornima

#Encapsulaction
--------------
--> Is the process of binding data and methods togather

class Bank:
    def __init__(self,balance):
        self.__balance = balance
        
    def depo_(self,amount):
        self.__balance += amount

    def get_bala(self):
        return self.__balance
acc=Bank(1000)
acc.depo_(10000)
print(acc.get_balance())

Output:
11000

'''





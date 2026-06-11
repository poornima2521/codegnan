'''
#polymorphism
->this means 'many forms'. it allows the same function,method or operator to behave differently depending on the object.
1.Method overloading
---------------------
->Method overloading means defining multiple methods with the same name but different paramaters.

eg 1
class calculator:
    def add(self,a,b):
        return a+b
an=calculator()
print(an.add(30,23))
print(an.add(30,23,9))
Output:
53

eg 2
class calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
an=calculator()
print(an.add(30,23))
print(an.add(30,23,9))
Output:
53
62

2.Method overriding
--------------------
->This occurs when a child class provides its own implementation of a method already defined in the parent class.

class animal:
    def sound (self):
        print("Animal makes sound")
class Dog(animal):
    def sound(self):
        print("Dog barks")

ntg=Dog()
ntg.sound()
Output:
Dogbarks
3.Operator overloading
-----------------------
->This allows operators such as +,-,*etc, to perform different actions for user-defined objects.
note:the other operator inside the method will overload a special 
eg 1

class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
so=stu(60)
any=stu(56)
print(so+any)
Output:
116

eg 2
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks*other.marks
so=stu(60)
any=stu(56)
print(so+any)

Output:
3360

Abstraction
------------
->This is the process of hiding internal implementation details and showing only essential features to the user.
->It focuses on what an object does rather than how t does it.


from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def parameters(self):
        return 2*(self.a*self.b)
an=Rec(10,5)
print(an.area())
Output:
50
-----------------------------------------------------------------Day20---------------------------------------------------------

#Error Handling


try block
---------
->The try block,test a block of code for error

except block
------------
->The except block let hand if the code contain errors

else block
----------
->This will be excuted,if the try block has no error in the code

finally block
-------------
->This will be excuted either try block contain error or not


try:
    print(10/0)
except:
    print("This will handle zerodivision error")
Op:
This will handle zerodivision error

try:
    print(a)
except:
    print("poornima")

Op:
poornima

try:
    print(9)
except:
    print(9+10)
OP:
9

try:
    print(len(a))
except:
    print("jbdbuisfiegfqbjqhfug")
OP:
jbdbuisfiegfqbjqhfug

try:
    print(10/0)
except:
    print("This will handle zerodivision error")
else:
    print("no error")
OP:
This will handle zerodivision error

try:
    a=10
    print(a+b)
except NameError:
    print("Name Error")
else:
    print("No Error")
    
op:Name Error->(A NameError occurs when you use a variable that has not been defined.)(here b is not defined)

    
    
try:
    a = 10+"5"
except TypeError:
    print("Type Error")
else:
    print(a)
    
op:Type Error->A TypeError occurs when an operation is performed on incompatible data types.(here used different data types)


try:
    print("hai")
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
    
op:hai
   no error
   end 
   

try:
    a=10
    print(b)
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
    
op:error
   end
   

try:
    d={1:"Apple",2:"Banana"}
    print(d[3])
except:
    print("error")
else:
    print("no error")
finally:
    print("end")

Output:
error
end


try:
    a={"A":"anu","B":"ani"}
    print(a["A"])
except:
    print("name  error")
else:
    print("no error")
finally:
    print("end")
OP:
anu
no error
end
'''







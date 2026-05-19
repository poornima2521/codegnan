'''
type conversions
----------------
int
--->Integer can be converted into string,float,
an=57
us=str(an)
om=float(an)
print(om)
print(type(om))
print(type(us))
output:


an="90"
hai=int(an)
print(type(hai))

an="python"
hai=int(an)
print(type(hai))
output:


an="90"
hai=float(an)
print(type(hai))

output:
    <class 'float'>

an="90"
hai=list(an)
print(type(hai))
output
<class 'list'>

an="90"
hai=tuple(an)
print(type(hai))

output:
    <class 'tuple'>

Float
----->
car=97.67
print(int(car))
print(str(car))
print(type(str(car)))
output:
    97
97.67
<class 'str'>

list
---->list converted into string and tuple.
any=[2,4]
print(str(any))
print(tuple(any))
output:
    [2, 4]
    (2, 4)
Tuple
-----
--->
hoe=(3,4)
print(list(hoe))

output:
    [3, 4]

num=int(input("Enter a number:"))
print(89+num)
output:
    Enter a number:67
156
tring as a user-input
---------------------





some=input("Write a text:")
output:write a text:python

str as a user-input
-------------------
any=list(map(int,input("Enter numbers:").split()))
print(any)
output:[23, 45, 67]
list as a user-input
--------------------

any=list(map(int,input("Enter numbers:").split()))
print(any)




tuple as a user-input
--------------------
'''
any=tuple(map(int,input("Enter numbers:").split()))
print(an)






'''
Built-in- functions
-------------------
print()
input()
len()
type()
max()
min()


m=[3,4,1,6,3]
m.sort()
print(m)
Output:
[1, 3, 3, 4, 6]

Recursive functions
------------------
-->A recursive function that calls it self to solve program by breaking into small or simple sub-problems.

def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
print(fac(5))

Output:120


def even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even(8)

Output:
even

Return
------
-->This ends a function execution and sends a value back to the code that called a function.

def add(a,b):
    return a+b
res= add(4,5)
print(res)

Output:
    9

Single line expresion or lambda function or anaomas function
--------------------------------------------------------
-->A lambda function is a small anonamus function.
-->A lambda can take n number of arguments,but only one expression
--->syntax-->lambda arguments: expression

so=lambda a,b,c: a+b+c+a
print(so(3,4,9))
Output:
    19

so=lambda a,b,c: a*b*c*a
print(so(3,4,6))

Output:216
'''
so=lambda a,b,c: a/b/c/a
print(so(3,4,6))

Output:
0.041666666666666664




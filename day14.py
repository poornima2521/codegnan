'''
Moduls
------
---> A moduls in python is a file that contains python code such as
--> variables
-->function
-->classes
-->statements

Two types of moduls
-------------------
user define
built-in



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
Output:
11
20

import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,5))
Output:
5.0
3628800
32.0

from math import sqrt
print(sqrt(25))

import math as m
print(m.factorial(10))
print(m.pow(2,5))


import os
os.mkdir("some_python")
Output:
file created in existed file
import os
os.rmdir("some_python")

Output:
file can be deleted from the existed file

import sys
print(sys.version)
print(sys.exit)
print(sys.path)
Output:
3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)]
<built-in function exit>
['C:/Users/Admin/Desktop/codegnan', 'C:\\Users\\Admin\\Documents', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\idlelib', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64\\python314.zip', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64\\DLLs', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64', 'C:\\Users\\Admin\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages']

import random
print(random.randint(1000,9999))

Output:3343


from collections import Counter
data=['a','b','c','d']
counter=Counter(data)
print(counter)
Output:
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})

'''
from collections import Counter,defaultdict
data=['a','b','c','d']
counter=Counter(data)

print(counter)
dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)

Output:
Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})
1
defaultdict(<class 'int'>, {'missing': 1})






'''
assert
-->this is debugging statement used to test whether a condition is true.
Assert Error


num=10
assert num>5
print("True")
Output:
    True
  
num=10
assert num<5
print("True")
output:
    AssertionError
 
age=19
assert age>=18,"age must be greater than or equal to 18"
print("eligible")
output:
    eligible

age=16
assert age>=18
print("eligible")
output:
   
    assert age>=18
AssertionError


Functions:
----------
--> a function is a block of code which ony execute when it is called
--> we can pas data, known as parameters into a function
-->To avoid repeated lines in code







def function_name(parameters):------>definition function
    ---------
    ----------
function_name(arguments)------>calling function



num=9
def even(num):
    print(num)
    even(num)
Output:
9

num=9
def even(num):
    if num %2==0:
        print(f"{num}even")
        else:
            print(f"{num}odd")
even(num)
even(109)

Output:
9odd
109odd

ways to arguments
----------------
1.Required arguments
---------------------
--> A function must be called with the same no of arguments
ex:
    
def even(num,num_2):
    if num %2==0:
        print(f"{num}even")
    else:
        print(f"{num}odd")

even(109,90)
Output:
109odd



2.Default arguments:
---------------------
-->BY DEFAult values is defined at parameters even thow it will take from arguments

def even(name="purni",age=89,sal=10):
    print(name)
    print(age)
    print(sal)
even("pappu",89,750000)
Output:
pappu
89
750000

Keyword arguments:
------------------------
--> we can said arguments with key=value syntax. By it is order of arguments does not matter...

def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even("name=pappu",age=89,sal=750000)
Output:
750000
name=pappu
89
Variable length arguments:
-------------------------
-->Adding a star(*) before the parameters name in the function,recieve a tuple of arguments and can access item with indexes. 
def even(*name):
    print(name[1])
even("Pooornima","sai","anu","hai")
Output:
sai
'''
name="purni"
def even(any):
    print(any)
even(name)
Output:
purni




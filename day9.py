'''
#NEESTED LOOP
--------------
for i in range (1,10):
    for j in range (1,2):
        print(i)
        print(j)

num=9
for j in range(1,11):
    print(f"{num}x{j}={j*num}")
output:
------    
9x1=9
9x2=18
9x3=27
9x4=36
9x5=45
9x6=54
9x7=63
9x8=72
9x9=81
9x10=90

so="python"
print(so[::-1])
output:
    nohtyp

so="python"
empty_str=""
for j in so:
    empty_str +=j
    print(empty_str)
Output:
    p
py
pyt
pyth
pytho
python


so=input("enter a wors:")
empty_str=""
for j in so:
    empty_str +=j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not pal")
output:
    enter a wors:madam
m
mam
mamdmam
mamdmamamamdmam
mamdmamamamdmammmamdmamamamdmam
madam is not pal

num=int(input("entera number:"))
amstro_=0
length=len(str(num))
for i in str(num):
    amstro_+=int(i)**length
if amstro_==num:
     print(f"{num} is a amsrong number")
else:
     print(f"{num} is not a amstrong number")
   
Output:
    entera number:153
153 is a amsrong number


num=28
per_no=0
for j in range(1,num):
    if num % j == 0:
        per_no=per_no+j
if per_no==num :
    print(f"{num} is a perfect num")
else:
    print(f"{num} is not a perfect num")
OUTPUT:
    28 is a perfect num

''
num=int(input("enter a number:"))
count=0
for k in range(1,num+1):
    if num % k==0:
        count +=1
if count ==2:
    print(f"{num} is a prime no")
else:
    print(f"{num} is not a prime")
Output:
    enter a number:13
13 is a prime no
    

star=5
for g in range(1,star+1):
    for d in range(1,g+1):
        print(chr(64+d),end=" ")
    print()
Output:
A
A B 
A B C 
A B C D 
A B C D E

star=5
count=0
for g in range(1,star+1):
    for d in range(1,g+1):
        count +=1
        print(count,end=" ")
    print()
Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 


star=5
count=0
for g in range(1,star+1):
    for d in range(1,g+1):
        count +=1
        print(d,end=" ")
    print()
Output:
1     
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

star=5
count=0
for g in range(star,0,-1):
    for d in range(g):
        count +=1
        print("*",end=" ")
    print()
Output:
* * * * * 
* * * * 
* * * 
* * 
* 
 
star=5
count=0
for g in range(star,0,-1):
    for d in range(g):
        count +=1
        print(d,end=" ")
    print()
output:
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0 
'''
num=5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()
Output:
    *
   * * 
  * * * 
 * * * * 
* * * * * 













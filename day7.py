'''condition statements
-----
if-->to check the statement is true or not


is-else-->else in the if statement,incase the condition becomes false then it will enter into flow-back(else),it will execute weather inside it

eg:

num=10
if num%2==0:
	print(f"{num}is a even number")
	print(f"(num)is a even {100} number")

num=int(input("Enter a number:"))
To find the num even or odd:
--------------------------
num=7
if num%2==0:
	print(f"{num}is a even number")
else:
	print(f"{num}is a even number")

output:
-------
7is a odd number


nested if
elif
To find to vote eligible:
------------------------

age_=int(input("Enter your age:"))
if age_>=18:
	print("we are eligible to vote")
else:
	print(f"we have to wait for {18-age}more years:)
output:
-------
Enter your age:21
we are eligible to vote

	
To find out small or not
---------------------
num=7
num_2=4
if num>=num_2:
	print(f"{num}is greater number than {num_2}")
else:
	print(f"{num}is greater number than {num}") 
output:
-------
7is greater number than 4

leap year
----------
year_=2024
if(year_%4==0 and year_% 100!= 0)or year_ % 400==0:
	print(f"{year_} is a leap year")
else:
	print(f"{year_} is not a leap year")
output:
--------
2024 is a leap year

To find vowel or not
------------
vowel_="a"
if vowel_in "AEIOUaeiou":
	print(f"{vowel_} is a vowel")
else:
	print(f"{vowel_} is a consonant")
output:
------  a is a vowel

To find positive and negative of a number
--------------- 
num=-9
if num>=0:
	print(f"{num} is a positive number")
else:
	print(f"{num} is a negative number")
output:
------
-9 is a negative number

To find pass or fail
------------------
marks_=int(input("enter your marks:"))
stu_name=input("enter your name:")
if marks_>=45:
	print(f"{stu_name} your passed")
else:
	print(f"{stu_name} your failed")

output:
-------
enter your marks:89
enter your name:poornima
poornima your passed


To find divisible by 3 and 5
----------

num=75
if num % 3 ==0 and num % 5 ==0:
	print(f"{num} is divided by 3 and 5")
else:
	print("f{num} is not")

output:75 is divided by 3 and 5


num=10
if num%2==0:
	print(f"{num}is a even number")
	print(f"(num)is a even {100} number")

num=int(input("Enter a number:"))
'''



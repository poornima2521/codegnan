'''
Regular expressions or (RegEx)
-----------------------------
-->RegEx is a sequence of character thatform a searching pattren.(meta charactres and functions used)
-->This can be used to check if a string contain the specified search pattren.
-->Python has a built-in package called 're' which can be used to work with RegEx.

Functions in RE
---------------
1.Findall
2.Search
3.Fullmatch

Meta characters
--------------
[]-->a-z,A-Z,0-9 and any specified sequence.
.--> Here each dot is one character.
^-->This look for the, string is starting with specified sequence or not.
$-->This look for the, string is ending with specified sequence or not. 
*-->Zero or more occurance
+-->one or more
{}-->where we can mention the position


Special Sequences
-----------------
"""
\\S ---> no space
\\s ---> only space
\\d ---> only digit
\\D ---> non-digit
\\w ---> word characters
\\W ---> non-word characters
"""
'''
import re
any = "c is a fundamental,general=purpose programming language created" # <re.Match object; span=(5, 6), match='a'>
print(re.search('[a]',any))

import re
any = "c is a fundamental,general=purpose programming language created"  # ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
print(re.findall('[a]',any))

import re
any = "c is a fundamental,general=purpose programming language created"
print(re.findall('[a-mA-Z]',any))

import re
any = "c is a fundamental,general=purpose  2638 programming 9394 language created34" # ['2', '6', '3', '8', '9', '3', '9', '4', '3', '4']
print(re.findall('[0-9]',any))  


import re
any = "c is a fundamental,general=purpose  2638 programming 9394 language created34" #['purpose']
print(re.findall('pu.p..e',any))

import re
any = "c is a fundamental,general=purpose  2638 programming 9394 language created34"  #<re.Match object; span=(27, 34), match='purpose'>
print(re.search('pu.p..e',any))

import re
any = "Python is a fundamental,general=purpose  2638 programming 9394 Python language created34"  #['Python']
print(re.search('^Python',any))

import re
any = "Python is a fundamental,general=purpose  2638 programming 9394 Python language created34"  #<re.Match object; span=(0, 6), match='Python'>
print(re.findall('^Python',any))



import re
any = "Python is a fundamental"   #['Python is a fundamental']
print(re.findall('P.*',any))

import re
any = "Python is a fundamental"    #['Python']
print(re.findall('P.?thon',any))

import re
any = "Python is a fundamental" #['Python i']
print(re.findall('P.{7}',any))

import re
any = "Python is a fundamental"  #['Python is']
print(re.findall('P.{8}',any))

import re
any = "Python is a fundamental"  #['Python is a fundamental']
print(re.findall('P.*',any))

import re
any = "Python is a fundamental"
print(re.findall('P.+thon',any))  #['Python']

import re
any = "Python is a fundamental"
print(re.findall(r'\S+',any))

import re
any = "Python is a fundamental"
print(re.findall(r'\s+',any))

import re
mobile = input("Enter 10 digit mobile number:")
hai=re.fullmatch('[6-9][0-9]{9}',mobile)
if hai:
    print(f"{mobile} this is india num")
else:
    print(f"{mobile} this is not india number")


import re
text = "Python is a fundamental"
print(re.findall(r'\S+', text))  # ['Python', 'is', 'a', 'fundamental']
print(re.findall(r'\s+', text))  # [' ', ' ', ' ']










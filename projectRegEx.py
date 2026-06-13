'''
Project based on regular expressions
-----------------------------------
Validation
----------
1.mobilenumber
--------------
-->10 digits init
2.passwors
----------
--> Cap,small,digit,special,character,atleast 8 digits
3.mail
--------
--> end with @gmail.com
'''

import re

class Validation:

    def mobile(self):
        num = input("Enter Mobile Number: ")
        if re.fullmatch(r"\d{10}", num):
            print("Valid Mobile Number")
        else:
            print("Invalid Mobile Number")

    def password(self):
        pwd = input("Enter Password: ")
        if (len(pwd) >= 8 and
            re.search(r"[A-Z]", pwd) and
            re.search(r"[a-z]", pwd) and
            re.search(r"\d", pwd) and
            re.search(r"[@#$%^&*!]", pwd)):
            print("Valid Password")
        else:
            print("Invalid Password")

    def email(self):
        mail = input("Enter Email: ")
        if re.fullmatch(r".+@gmail\.com", mail):
            print("Valid Gmail")
        else:
            print("Invalid Gmail")


obj = Validation()

while True:
    print("\n1. Mobile Validation")
    print("2. Password Validation")
    print("3. Email Validation")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        obj.mobile()

    elif choice == "2":
        obj.password()

    elif choice == "3":
        obj.email()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

   

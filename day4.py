'''
list

concatination
-------------
-->The (+) for int and can add,but for the other data types it will act as concatinating the data types.

list
a=90
b=8
print(a+b)
any_="pyrhon"
so="is a language"
print(any_+so)
an=[1,2]
am=[3,4]
print(an+am)

Tuple
-----
-->Collection of different data types separated by comms,reprasented in () and immutable.

some=(1,"python",[1,2],(3,4))
print(some)
output:
methods
-------
count()
------
-->this used to count the particular item in the tuple

syntax
------
-->variable_name.count(item)
example
------
some=(1,"python",[1,2],(3,4),"python")
print(some.count("python"))
output:2

index()
-------
-->usedto find out the index position of the item,and only gives the first occurance

some=(1,[1,2],(3,4),"python")
print(some.index("python"))
output:3

some=(25,[79,4],"hai","sai",(3,6))
print(some.index("hai"))

output:2

Dictionary
---------
-->it is a key : value pair,key and values  separated by : and pair separated by comma.
-->reprasented by {}

sai_details={"Name":"Sai",11:2,(1,2):[3,4]}
print(type(sai_details))


Methods
------

sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
print(sai_details.keys())

output:dict_keys(['Name', 'age', 'MobN', 'pan'])

Values()

sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
print(sai_details.values())
output:dict_values(['Sai', 20, '123456780', 'hgdjaloi'])

Items()
-------
-->usedtoget key and value togather
-->syntax---->dict.items()

sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
print(sai_details.items())
print(sai_details["age"])
output:dict_items([('Name', 'Sai'), ('age', 20), ('MobN', '123456780'), ('pan', 'hgdjaloi')])
20

update()
-------
-->used to add new key :value pair into dict
--->syntax---->dict.update({key:value})

sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
sai_details.update({"Adhar":"286665012352"})
sai_details['Name']="poorni"
print(sai_details["age"])
output:20

sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
sai_details.update({"Adhar":"286665012352"})
sai_details['Name']="poorni"
print(sai_details)
output:{'Name': 'poorni', 'age': 20, 'MobN': '123456780', 'pan': 'hgdjaloi', 'Adhar': '286665012352'}

clear()
------
-->used to remove all the items in the dict
'''
sai_details={"Name":"Sai",
             "age":20,
             "MobN":"123456780",
             "pan":"hgdjaloi"}
sai_details.clear()
print(sai_details)
output:{}













'''
set
---
--->A set is collection of unique and unordered elements.
--->Duplicate values are not allowed.
--->items are not stored in index order
--->Reprasented in{}
ex-
---
any={1,2,3,4,4}
print(any)
output:{1, 2, 3, 4}


methods
-------
union()
-----
-->It will give all values from 2 sts together in once
-->syntsx-->variable_name.union(another variable)
ex
--
any={1,2,3,4,4}
an={56,67}
print(any | an)
print(any.union(an))
output:{1, 2, 3, 4, 67, 56}
{1, 2, 3, 4, 67, 56}

ex
any={1,2,3,4,4}
an={64,89}
print(any | an)
print(any.union(an))

output:{64, 1, 2, 3, 4, 89}
{64, 1, 2, 3, 4, 89}



Intersection()
-----------
--->To get the common elements from both sets
-->Syntax
variable_name.intersection(another variable)
any={1,2,3,4,4}
an={64,89,3,1}
print(any.intersection(an))

output
-----
{1, 3}

Difference()
------------
syntax-->variable_name.difference(another variable)

any={1,2,3,4,4}
an={64,89,3,1}
print(any.difference(an))
output
------
{2, 4}

any={1,2,3,4,4}
an={64,89,3,1}
print(any-an)
print(any.difference(an))

output
{2, 4}
{2, 4}

any={1,2,3,4,4}
an={64,89,3,1}
print(any-an)
print(an.difference(any))
output
------
{2, 4}
{64, 89}

1.symetric difference
2.

Functions()
--->

add()
-----
---> Toadd new elements into set
syntx-->variable_name.add(element)
ex
any={2,3,4,5,5}
any.add(56)
print(any)
output
-----
{2, 3, 4, 5, 56}


update()
-------
--->To add multipule elements into set
---->syntax
ex
any={2,3,4,5,5}
any.update([56,78])
print(any)
output
------
{2, 3, 4, 5, 78, 56}

sum,len,min,max
ex

any={2,3,4,5,5}
print(min(any))
print(sum(any))
print(len(any))

output
2
14
4
remove()
------
--->used to remove element from the set.but it through error if element not in set
syntax-->variable_name.remove(element)
any={2,3,4,5,5}
any.remove(2)
print(any)
output
------
{3, 4, 5}

discard()
---------
--->used to remove element from the set
-->syntax-->any.discard(element)

any={2,3,4,5,5}
any.discard(2)
print(any)

output
-----
{3, 4, 5}

'''













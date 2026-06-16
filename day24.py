'''
Data Analasis
-------------
-->This is the process of inspectting ,cleaning ,transforming and modeling data to discover useful insights..
Types of Data anlatics
----------------------
1.Discriptive Analysis
----------------------
--> Summarizing Data

2.Diagnostic Analysis
----------------------
--> Understanding causes

3.predictive Analysis
---------------------
--> Forecsting future outcomes

4.perspective Analysis
-----------------------
-->Suggesting actions based on data

Why Data analysis
------------------
--> To improve decision making
--> Detects trends and pattren

Libraries
--------

Numpy(Numerical python)
----------------------
--> This python library for numerical computing.it provides for support multi-dimensional arrays,and linear algebra operations of
making essential for data analysis.
--> array concepts in python.
using numpy in Da
-----------------
--> Improved performance
-->Simplifies complex operations
-->Easy data manipulation
-->take rows and co;ums are same otherwise error coming.
-->indexing,slicing also applicable


pandas
------
--> The pandas is a powerfull data manipulation and analysis library.
--> Where it provides data structure like series and dataframes foe efficiencey data 
Methods Series
--------------
mean()
sum()
max()
min()
apply()
map()
Dataframe
----------

'''
#One dimensional
import numpy as np
arr_1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_1)

#two dimenstional
import numpy as np
arr_1 = np.array([[2,3,4],[5,6,7,]])
print(arr_1)
print(arr_1.shape)
reshaped = arr_1.reshape(3,2)
print(reshaped)
#indexing
import numpy as np
arr_1=np.array([10,2,3,45,6])
print(arr_1[2])

#mathematical operations
import numpy as np
arr_1=np.array([10,2,3,45,6])
print(arr_1+5)

import numpy as np
arr_1=np.array([10,2,3,45,6])
print(arr_1*5)

#matrix (shape)
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(np.dot(arr1,arr2))

# shallow copy
import numpy as np
arr1=np.array([10,20,30])
nrm_copy=arr1.view()
arr1[0]=100
print(nrm_copy)
print(arr1)

#deep copy
import numpy as np
arr1=np.array([10,20,30])
copy_dee=arr1.copy()
arr1[1]=200
print(copy_dee)
print(arr1)

#pandas
import pandas as pd
any=pd.Series([2999,15999,52999,4999,1999],index=['Earbuds','Smartphone','Laptop','Watch','Footware'])
print(any)                                                  

#Draframe
import pandas as pd

data = {
    'product': ['Earbuds', 'Smartphone', 'Laptop', 'Watch', 'Footwear'],
    'brand': ['Noise', 'OnePlus', 'HP', 'Boat', 'Nike'],
    'price': [1599, 15999, 53999, 1999, 3999],
    'stock': [50, 15, 25, 40, 70]
}

df = pd.DataFrame(data)
print(df)      
                























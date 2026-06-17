
'''
Matplotlib
----------

#Matplotlib is a Python library used for data visualization.

Basic Structures of Matplotlib
------------------------------
1. Figure  - Entire window or canvas
2. Axes    - Plot area
3. Axis    - X-axis and Y-axis
4. Grid    - Background reference lines
5. Title   - Heading of the graph
6. Legend  - Explains data series

#Bar Graph

import matplotlib.pyplot as plt

sales = ['A', 'B', 'C']
values = [25, 30, 45]

plt.bar(sales, values, color='red', edgecolor='black')
plt.xlabel('Company Models')
plt.ylabel('Values')
plt.title('BMW Sales')
plt.show()

#Line Graph

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y, color='yellow')
plt.title('Score Card')
plt.xlabel('Overs')
plt.ylabel('Scores')
plt.show()

#Pie Chart

import matplotlib.pyplot as plt
subjects = ['Python', 'Java', 'C']
students = [35, 7, 15]
plt.pie(students, labels=subjects)
plt.title('Students in Courses')
plt.show()

#Pie Chart with Percentage

import matplotlib.pyplot as plt
subjects = ['Python', 'Java', 'C']
students = [35, 7, 15]
plt.pie(students, labels=subjects, autopct='%1.1f%%')
plt.legend(subjects)
plt.title('Students in Courses')
plt.show()

#Scatter Plot

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 13, 18, 25, 13]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()

#Histogram Plot

import matplotlib.pyplot as plt
y = [10, 13, 18, 25, 13]
plt.hist(y)
plt.title('Histogram Plot')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

#To write the program for a company sales in years in a bar graph
'''
import matplotlib.pyplot as plt


# Data
years = [2020, 2021, 2022, 2023, 2024]
sales = [50000, 65000, 80000, 75000, 90000]

# Bar graph
plt.bar(years, sales,color='yellow',edgecolor='green')

# Title and labels
plt.title("ABC Company Sales Report")
plt.xlabel("Years")
plt.ylabel("Sales")

# Display graph
plt.show()













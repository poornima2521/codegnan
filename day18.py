
#To print the details of a student and faculty in a university with the help of opps concepts.   

class Person:
    university_name = "Maharaja University"

    def __init__(self, name, age, Edu_Bg, gender, department):
        self.name = name
        self.age = age
        self.Edu_Bg = Edu_Bg
        self.gender = gender
        self.department = department

    def display_info(self):
        pass


class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course,
                 year_, Edu_Bg, gender, department):

        super().__init__(name, age, Edu_Bg, gender, department)

        self.student_id = student_id
        self.course = course
        self.year_ = year_

        Student.student_count += 1

    def display_info(self):
        print("\n----- Student Details -----")
        print(f"University : {Person.university_name}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Student ID : {self.student_id}")
        print(f"Course     : {self.course}")
        print(f"Year       : {self.year_}")
        print(f"Education  : {self.Edu_Bg}")
        print(f"Gender     : {self.gender}")
        print(f"Department : {self.department}")


class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, Edu_Bg,
                 gender, department, experience):

        super().__init__(name, age, Edu_Bg, gender, department)

        self.experience = experience

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n----- Faculty Details -----")
        print(f"University : {Person.university_name}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Education  : {self.Edu_Bg}")
        print(f"Gender     : {self.gender}")
        print(f"Department : {self.department}")
        print(f"Experience : {self.experience}")

student1 = Student(
    "Poornima",
    20,
    "23A1CSC179",
    "B.Sc Computer Science",
    "3rd Year",
    "Intermediate",
    "Female",
    "CS"
)
faculty1 = Faculty(
    "Mounika",
    45,
    "M.Tech",
    "Female",
    "CS",
    "3 Years"
)

student1.display_info()
faculty1.display_info()

print("\nTotal Students:", Student.student_count)
print("Total Faculty :", Faculty.faculty_count)

Output:
----- Student Details -----
University : Maharaja University
Name       : Poornima
Age        : 20
Student ID : 23A1CSC179
Course     : B.Sc Computer Science
Year       : 3rd Year
Education  : Intermediate
Gender     : Female
Department : CS

----- Faculty Details -----
University : Maharaja University
Name       : Mounika
Age        : 45
Education  : M.Tech
Gender     : Female
Department : CS
Experience : 3 Years

Total Students: 1
Total Faculty : 1

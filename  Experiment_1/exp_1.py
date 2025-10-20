# 1.2 Write a program to illustrate various data types & concepts of variables/Constant in Python.

# Variables (dynamic typing)
name = "Alice" # String
age = 25 # Integer
height = 5.6 # Float
is_student = True # Boolean
subjects = ["Math", "CS"] # List
marks = (85, 90, 88) # Tuple
info = {"id": 101, "dept": "CSE"} # Dictionary
hobbies = {"reading", "coding"} # Set

# Displaying types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
print("Subjects:", subjects, "| Type:", type(subjects))
print("Marks:", marks, "| Type:", type(marks))
print("Info:", info, "| Type:", type(info))
print("Hobbies:", hobbies, "| Type:", type(hobbies))

# Constants (by convention in UPPERCASE)
PI = 3.14159
GRAVITY = 9.81
print("Constant PI:", PI)
print("Constant GRAVITY:", GRAVITY)
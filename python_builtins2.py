"""
Python Built-in Functions Practice File
Author: Mohammed Sinan

This file demonstrates:
len, range, enumerate, zip, map, filter, sorted, reversed,
sum, min, max,
int, float, str, list, tuple, set, dict, bool,
print, type, isinstance, dir, id,
any, all, open, getattr, setattr, callable, vars
"""

# ============================================================
# 1. len()
# ============================================================

students = ["Ali", "John", "Sara", "David"]

# len() returns the number of elements in a collection
print("Total students:", len(students))


# ============================================================
# 2. range()
# ============================================================

# range(start, stop, step)
for number in range(1, 6):
    print("Range value:", number)


# ============================================================
# 3. enumerate()
# ============================================================

# enumerate gives index and value together
for index, student in enumerate(students):
    print(f"Index={index}, Name={student}")


# ============================================================
# 4. zip()
# ============================================================

marks = [85, 92, 78, 88]

# zip combines multiple iterables element by element
student_marks = list(zip(students, marks))

print("Zipped data:", student_marks)


# ============================================================
# 5. map()
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Apply square operation to every element
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Squared:", squared_numbers)


# ============================================================
# 6. filter()
# ============================================================

# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)


# ============================================================
# 7. sorted()
# ============================================================

words = ["banana", "kiwi", "apple", "watermelon"]

# Sort by word length
sorted_words = sorted(words, key=lambda word: len(word))

print("Sorted by length:", sorted_words)


# ============================================================
# 8. reversed()
# ============================================================

reversed_words = list(reversed(words))

print("Reversed words:", reversed_words)


# ============================================================
# 9. sum()
# ============================================================

total_marks = sum(marks)

print("Total marks:", total_marks)


# ============================================================
# 10. min() and max()
# ============================================================

print("Minimum mark:", min(marks))
print("Maximum mark:", max(marks))


# ============================================================
# 11. Type Conversion Functions
# ============================================================

number_string = "100"

# String -> Integer
integer_value = int(number_string)

# String -> Float
float_value = float("99.5")

# Integer -> String
string_value = str(500)

# String -> List
character_list = list("python")

# List -> Tuple
tuple_data = tuple([1, 2, 3])

# List -> Set (removes duplicates)
set_data = set([1, 1, 2, 2, 3, 3])

# List of tuples -> Dictionary
dict_data = dict([
    ("name", "Ali"),
    ("age", 22)
])

# Any value -> Boolean
bool_data = bool(1)

print(integer_value)
print(float_value)
print(string_value)
print(character_list)
print(tuple_data)
print(set_data)
print(dict_data)
print(bool_data)


# ============================================================
# 12. print()
# ============================================================

print("Hello Python")


# ============================================================
# 13. type()
# ============================================================

print(type(100))
print(type("hello"))
print(type([1, 2, 3]))


# ============================================================
# 14. isinstance()
# ============================================================

print(isinstance(100, int))
print(isinstance("python", str))
print(isinstance([1, 2], list))


# ============================================================
# 15. dir()
# ============================================================

# Shows available methods and attributes
print("Some string methods:")
print(dir(str)[:10])


# ============================================================
# 16. id()
# ============================================================

data = [1, 2, 3]

# Unique memory identity
print("Object ID:", id(data))


# ============================================================
# 17. any()
# ============================================================

attendance = [False, False, True, False]

# Returns True if at least one item is True
print("Any present:", any(attendance))


# ============================================================
# 18. all()
# ============================================================

exam_passed = [True, True, True]

# Returns True only if all are True
print("All passed:", all(exam_passed))


# ============================================================
# 19. callable()
# ============================================================

print("Is len callable?", callable(len))
print("Is 100 callable?", callable(100))


# ============================================================
# 20. Object-Oriented Example
# Used for getattr, setattr, vars
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}"


student = Student("Sinan", 22)


# ============================================================
# 21. getattr()
# ============================================================

# Dynamically access attributes
student_name = getattr(student, "name")

print("Student name:", student_name)


# ============================================================
# 22. setattr()
# ============================================================

# Dynamically create/update attributes
setattr(student, "college", "ABC University")

print(student.college)


# ============================================================
# 23. vars()
# ============================================================

# Returns object's attribute dictionary
print(vars(student))


# ============================================================
# 24. open()
# ============================================================

# Write data to a file
with open("sample.txt", "w") as file:
    file.write("Hello from Python\n")
    file.write("Built-in functions practice\n")

# Read data from the file
with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# ============================================================
# Medium-Level Real Example
# Combining enumerate, zip, sorted, lambda, max, sum
# ============================================================

employees = [
    ("Ali", 85000),
    ("John", 92000),
    ("Sara", 78000),
    ("David", 98000)
]

# Highest paid employee
highest_paid = max(
    employees,
    key=lambda employee: employee[1]
)

print("Highest paid:", highest_paid)

# Total salary expense
salary_expense = sum(
    salary
    for _, salary in employees
)

print("Salary expense:", salary_expense)

# Sort employees by salary descending
sorted_employees = sorted(
    employees,
    key=lambda employee: employee[1],
    reverse=True
)

print("Sorted employees:")
for rank, employee in enumerate(sorted_employees, start=1):
    print(rank, employee)

# Convert to dictionary
employee_dict = dict(employees)

print(employee_dict)

# Check if anyone earns above 95000
print(
    any(
        salary > 95000
        for salary in employee_dict.values()
    )
)

# Check if everyone earns above 50000
print(
    all(
        salary > 50000
        for salary in employee_dict.values()
    )
)

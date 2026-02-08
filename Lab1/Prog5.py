# 5. Program on Dictionaries in Python File
# Dictionary of courses and number of students enrolled
courses = {
    "Python": 120,
    "Java": 95,
    "C++": 80,
    "Data Science": 150,
    "Machine Learning": 130
}

print("Original Dictionary:")
print(courses)

# 1. Accessing value using get()
print("\nStudents in Java:", courses.get("Java"))

# 2. Adding a new course
courses["Cyber Security"] = 90
print("\nAfter Adding Cyber Security:")
print(courses)

# 3. Updating students in an existing course
courses.update({"Python": 125})
print("\nAfter Updating Python Students:")
print(courses)

# 4. Removing a course using pop()
removed = courses.pop("C++")
print(f"\nRemoved C++ with {removed} students")
print(courses)

# 5. Removing last inserted item using popitem()
last_item = courses.popitem()
print(f"\nRemoved last inserted item: {last_item}")
print(courses)

# 6. Displaying all keys, values, and items
print("\nCourses:", courses.keys())
print("Students:", courses.values())
print("Course-Student Pairs:", courses.items())

# 7. Checking if a course exists
if "Java" in courses:
    print("\nJava course is available")

# 8. Copying dictionary
copy_dict = courses.copy()
print("\nCopied Dictionary:", copy_dict)

# 9. Clearing dictionary
courses.clear()
print("\nDictionary after clearing:", courses)
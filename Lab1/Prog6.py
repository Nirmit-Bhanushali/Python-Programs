# 6. Program to implement Normal function and Lambda function File

# Normal function to get full name of a student
def full_name(first_name, last_name):
    return first_name + " " + last_name

# Lambda function to calculate percentage
percentage = lambda obtained, total: (obtained / total) * 100

# student data
students = [
    {"first": "Amit", "last": "Sharma", "marks": 450, "total": 500},
    {"first": "Riya", "last": "Patil", "marks": 380, "total": 500},
    {"first": "Siddhi", "last": "Mukadam", "marks": 420, "total": 500}
]

# Using functions
for s in students:
    name = full_name(s["first"], s["last"])          # normal function
    perc = percentage(s["marks"], s["total"])        # lambda function
    print(f"Student: {name} | Percentage: {perc:.2f}%")
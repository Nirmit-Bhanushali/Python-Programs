# 8. Program to demonstrate the use of Matplotlib Library in Python File
# Usage of Matplotlib

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# 1. Line Plot
plt.figure(1)   # create first figure
plt.plot(x, y, label="y = 2x", color='blue', marker='o')
plt.plot(x, y2, label="y = x²", color='red', linestyle='--')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")
plt.legend()

# 2. Bar Chart
plt.figure(2)   # create second figure
students = ["Aparna", "Monica", "Rohit", "Sagar"]
marks = [85, 70, 90, 60]
plt.bar(students, marks, color='green')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Chart Example")

# 3. Scatter Plot
plt.figure(3)   # create third figure
plt.scatter(x, y2, color='purple')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")

# Show all plots
plt.show()
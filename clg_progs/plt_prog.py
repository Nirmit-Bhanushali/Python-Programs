import matplotlib.pyplot as plt

# x values
x = [1, 2, 3, 4, 5]

# sample y values (kept as provided)
y = [9, 8, 7, 4, 5]

# compute y2 as x squared so lengths match x and the label is correct
y2 = [1,5,8,9,2]

# 1. Line Plot
plt.figure(1)
# plot the two lines
plt.plot(x, y, label="y (sample)", color='blue', marker='o')
plt.plot(x, y2, label="x²", color='red', linestyle='--')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")
plt.legend()

#2. Bar Chart
plt.figure(2) # create second figure 
students = ["Aparna", "Monica", "Rohit", "Sagar"] 
marks = [85, 70, 90, 60]

plt.bar(students, marks, color='green')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Bar Chart Example")

# 3. Scatter Plot
plt.figure(3) # create third figure 
plt.scatter(x, y2, color='purple') 
plt.xlabel("X values") 
plt.ylabel("Y values") 
plt.title("Scatter Plot Example")

# Show all plots 
plt.show()
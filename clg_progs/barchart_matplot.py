# .  Use the Matplotlib library to plot a simple Bar Chart showing the monthly sales figures (dummy data) for the last six months. Ensure the chart has labeled axes and a title.
import matplotlib.pyplot as plt

# Dummy sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [150, 200, 180, 220, 170, 210]

# Plotting the bar chart
plt.bar(months, sales, color="skyblue", edgecolor="black")

# Adding labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Figures (Last 6 Months)")

# Display the chart
plt.show()
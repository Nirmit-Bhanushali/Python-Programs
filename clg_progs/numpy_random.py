# Use the NumPy library to create an array of 50 random floating-point numbers. Use the Matplotlib library to generate a simple line plot of these numbers.
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create an array of 50 random floating-point numbers
data = np.random.rand(50)  # values between 0 and 1

# Step 2: Generate a simple line plot
plt.plot(data, marker='o', linestyle='-', color='blue')

# Step 3: Add labels and title
plt.xlabel("Index")
plt.ylabel("Random Value")
plt.title("Line Plot of 50 Random Floating-Point Numbers")

# Step 4: Display the plot
plt.show()
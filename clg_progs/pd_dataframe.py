# Create a Pandas DataFrame from a dictionary containing names, ages, and cities for five employees. Display the first three rows of the DataFrame and then filter and print only the employees aged 30 or above

import pandas as pd

# Create a dictionary with employee data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 32, 29, 40, 30],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the first three rows
print("First three rows of the DataFrame:")
print(df.head(3))

# Filter employees aged 30 or above
print("\nEmployees aged 30 or above:")
print(df[df["Age"] >= 30])

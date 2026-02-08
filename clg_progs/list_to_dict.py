# Create a Python program that defines a list of fruits. Use a for loop to iterate through the list and store the fruit name and its length (as a string) in a dictionary. Print the final dictionary.
# Program to store fruit names and their lengths in a dictionary

# Define a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

# Create an empty dictionary
fruit_dict = {}

# Iterate through the list and store fruit name and its length
for fruit in fruits:
    fruit_dict[fruit] = str(len(fruit))  # length stored as string

# Print the final dictionary
print("Fruit dictionary with lengths:")
print(fruit_dict)
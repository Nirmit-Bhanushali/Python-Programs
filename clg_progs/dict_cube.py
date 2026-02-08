# Write a Python program that takes a list of integers, removes all duplicate values, and stores the unique elements in a tuple. Then, convert the tuple into a dictionary where the keys are the elements and the values are the cube of the elements.
# Program to remove duplicates, store unique elements in a tuple,
# and convert to a dictionary with cubes as values

# Step 1: Define a list of integers (you can change this list)
numbers = [2, 3, 4, 2, 5, 3, 6, 4]

# Step 2: Remove duplicates by converting to a set, then back to a list
unique_list = list(set(numbers))

# Step 3: Store unique elements in a tuple
unique_tuple = tuple(unique_list)
print("Unique elements tuple:", unique_tuple)

# Step 4: Convert tuple into dictionary {element: cube}
cube_dict = {num: num**3 for num in unique_tuple}
print("Dictionary with cubes:", cube_dict)
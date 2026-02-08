# 4. Program to implement Tuples in Python File
# Creating a tuple of Indian names
names = ("Aarav", "Isha", "Rohan", "Priya", "Aarav")

print("Tuple of names:", names)

# Accessing elements
print("\nFirst name:", names[0])         # Access by index
print("Last name:", names[-1])           # Negative indexing
print("Slice [1:4]:", names[1:4])        # Slicing

# Tuple methods
print("\nCount of 'Aarav':", names.count("Aarav"))   # Count occurrences
print("Index of 'Rohan':", names.index("Rohan"))     # Find index

# Traversing through tuple
print("\nTraversing names:")
for name in names:
    print(name)

# Checking membership
print("\nIs 'Priya' in tuple?", "Priya" in names)
print("Is 'Kiran' in tuple?", "Kiran" in names)

# Tuple concatenation
more_names = ("Kiran", "Meera")
combined = names + more_names
print("\nConcatenated tuple:", combined)

# Tuple repetition
repeated = names * 2
print("Repeated tuple:", repeated)

# Length of tuple
print("\nLength of names tuple:", len(names))

# Converting tuple to list (since tuples are immutable)
names_list = list(names)
names_list.append("Raj")
print("\nConverted to list and added 'Raj':", names_list)

# Converting back to tuple
names = tuple(names_list)
print("Back to tuple:", names)
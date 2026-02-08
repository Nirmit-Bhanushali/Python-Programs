
# 3. Program to demonstrate Lists File
# Operations on a list

# Create a list
numbers = [45, 15, 10, 50, 12]
print("Original List:", numbers)

# Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Insert an element
numbers.append(60)
print("After appending 60:", numbers)

# Insert at specific position
numbers.insert(2, 25)
print("After inserting 25 at index 2:", numbers)

# Delete an element
numbers.remove(45)
print("After removing 45:", numbers)

# Update an element
numbers[1] = 15
print("After updating second element to 15:", numbers)

# Search for an element
if 30 in numbers:
    print("30 is present in the list.")
else:
    print("30 is not in the list.")

# Length of the list
print("Length of the list:", len(numbers))
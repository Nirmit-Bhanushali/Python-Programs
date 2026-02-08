# 2. Program to implement decision making
# Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even.")
else:
    print(num, "is Odd.")


# Find the largest among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)



# Grade calculation based on marks

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")
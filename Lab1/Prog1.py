# 1.Perform Basic arithmetic operations and find factorial of a given number File

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operators ---")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")

print("\n--- Assignment Operators ---")
c = a
print(f"Initial value of c: {c}")
c += b
print(f"c += b → {c}")
c -= b
print(f"c -= b → {c}")
c *= b
print(f"c *= b → {c}")
c /= b
print(f"c /= b → {c}")

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
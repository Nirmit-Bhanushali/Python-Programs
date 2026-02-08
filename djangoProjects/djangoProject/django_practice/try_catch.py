try:
    num = float(input("Enter a positive number: "))

    if num < 0:
        raise ValueError("Negative number not allowed")
    print("You entered:", num)

except ValueError:
    print("Error: Please enter only positive values!")


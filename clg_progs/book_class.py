# Design a Python class named Book with attributes like title, author, and price. Implement a constructor, a method to display book details, and demonstrate inheritance by creating a subclass Ebook that adds an attribute file_size.
# Define the Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price}")

# Define the Ebook subclass (inherits from Book)
class Ebook(Book):
    def __init__(self, title, author, price, file_size):
        # Call the parent constructor
        super().__init__(title, author, price)
        self.file_size = file_size

    # Override display_details to include file_size
    def display_details(self):
        super().display_details()  # Call parent method
        print(f"File Size: {self.file_size} MB")

# Demonstration
# Create a Book object
book1 = Book("Python Basics", "John Doe", 499)
print("Book Details:")
book1.display_details()

print("\nEbook Details:")
# Create an Ebook object
ebook1 = Ebook("Advanced Python", "Jane Smith", 299, 5)
ebook1.display_details()
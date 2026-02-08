# 7. Program to implement Class inheritance in Python File

# 1. Single Inheritance

class Stationery:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f"Stationery: {self.name}, Price: ₹{self.price}")

class Pen(Stationery):  # Single Inheritance
    def __init__(self, name, price, ink_color):
        super().__init__(name, price)
        self.ink_color = ink_color
    
    def display_info(self):
        super().display_info()
        print(f"Ink Color: {self.ink_color}")


# 2. Multiple Inheritance

class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name
    
    def show_brand(self):
        print(f"Brand: {self.brand_name}")

class Marker(Stationery, Brand):  # Multiple Inheritance
    def __init__(self, name, price, tip_size, brand_name):
        Stationery.__init__(self, name, price)
        Brand.__init__(self, brand_name)
        self.tip_size = tip_size
    
    def display_info(self):
        super().display_info()
        self.show_brand()
        print(f"Tip Size: {self.tip_size} mm")


# 3. Multilevel Inheritance

class WritingInstrument(Stationery):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type
class Pencil(WritingInstrument):  # Multilevel (Stationery → WritingInstrument → Pencil)
    def __init__(self, name, price, hardness):
        super().__init__(name, price, "Pencil")
        self.hardness = hardness
    
    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}, Hardness: {self.hardness}")

# 4. Hierarchical Inheritance

class Eraser(Stationery):  # Child 1
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material
    
    def display_info(self):
        super().display_info()
        print(f"Material: {self.material}")

class Sharpener(Stationery):  # Child 2
    def __init__(self, name, price, blade_type):
        super().__init__(name, price)
        self.blade_type = blade_type
    
    def display_info(self):
        super().display_info()
        print(f"Blade Type: {self.blade_type}")

# 5. Hybrid Inheritance (Combination)

class Highlighter(Marker, WritingInstrument):  # Multiple + Multilevel → Hybrid
    def __init__(self, name, price, ink_color, brand_name):
        Marker.__init__(self, name, price, 1.0, brand_name)  # Marker properties
        WritingInstrument.__init__(self, name, price, "Highlighter")  # WritingInstrument
        self.ink_color = ink_color
    
    def display_info(self):
        super().display_info()
        print(f"Ink Color: {self.ink_color} (Fluorescent)")
        print(f"Type: {self.type}")

# Testing All Inheritance Types

print("---- Single Inheritance ----")
pen = Pen("Ball Pen", 10, "Blue")
pen.display_info()

print("\n---- Multiple Inheritance ----")
marker = Marker("Whiteboard Marker", 30, 2, "Camlin")
marker.display_info()

print("\n---- Multilevel Inheritance ----")
pencil = Pencil("Apsara Pencil", 5, "HB")
pencil.display_info()

print("\n---- Hierarchical Inheritance ----")
eraser = Eraser("Natraj Eraser", 3, "Rubber")
eraser.display_info()

sharpener = Sharpener("Domes Sharpener", 7, "Steel Blade")
sharpener.display_info()

print("\n---- Hybrid Inheritance ----")
highlighter = Highlighter("Faber-Castell Highlighter", 40, "Yellow", "Faber-Castell")
highlighter.display_info()

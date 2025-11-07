# Python Practice File - dunder_methods

# 1. __init__ (Constructor)
class Book:
    """
    The __init__ method is automatically called when a new object is created.
    It initializes the instance attributes.
    """
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        print(f"Book '{self.title}' object created.")

print("--- 1. __init__ Example ---")
my_book = Book("The Python Way", 500)

print("-" * 20)

# 2. __str__ (String Representation) and __repr__ (Official Representation)
class Person:
    """
    __str__ is used for readable representation (for end-users, like print()).
    __repr__ is used for official string representation (for developers/debugging).
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Jagadish", 34)

print("--- 2. __str__ and __repr__ Example ---")
print(f"Using print() (__str__): {p}") # Calls __str__
print(f"Using repr() (__repr__): {repr(p)}") # Calls __repr__

print("-" * 20)

# 3. __len__ (Length)
class CustomList:
    """Allows the built-in len() function to work on this object."""
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

my_list_obj = CustomList([10, 20, 30, 40, 50])

print("--- 3. __len__ Example ---")
print(f"Data: {my_list_obj.data}")
print(f"Length of the object (using len()): {len(my_list_obj)}")

print("-" * 20)

# 4. __add__ (Operator Overloading)
class Vector:
    """Overloads the '+' operator using the __add__ dunder method."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Defines what happens when V1 + V2 is executed
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
        
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

V1 = Vector(5, 10)
V2 = Vector(1, 2)
V3 = V1 + V2  # This calls V1.__add__(V2)

print("--- 4. __add__ Example (Operator Overloading) ---")
print(f"Vector 1: {V1}")
print(f"Vector 2: {V2}")
print(f"Vector 1 + Vector 2: {V3}")
# Python Practice File - classes_objects

# 1. Basic Class and Object Creation
class BasicCalculator:
    # A simple method
    def multiply(self, a, b):
        return a * b

# Create an object (instance) of the class
calc_obj = BasicCalculator()
result = calc_obj.multiply(5, 7)
print(f"1. Basic multiplication result: {result}")

print("-" * 20)

# 2. Class with Constructor (__init__) and Instance Attributes/Methods
class Student:
    # Class attribute (shared by all instances)
    school_name = "Tech Academy"

    # Constructor method to initialize object state
    def __init__(self, name, roll_no, score):
        # Instance attributes (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.score = score
    
    # Instance method (operates on object data)
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Score: {self.score}")
        print(f"School: {self.school_name}") # Accessing class attribute

# Create objects
neon = Student("Jagadish", "KJ1", 500)
sanya = Student("Sanyasi", "SR2", 450)

print("2. Student Info (Instance Attributes/Methods):")
neon.show_info()

print("-" * 20)

# 3. Class Methods and Static Methods
class Animal:
    # Class attribute
    total_animals = 0

    def __init__(self, species):
        self.species = species
        Animal.total_animals += 1

    # Class method (uses @classmethod and receives the class itself as the first argument 'cls')
    @classmethod
    def get_total_count(cls):
        """Reports on a class-level variable."""
        print(f"Total animal objects created: {cls.total_animals}")

    # Static method (uses @staticmethod and takes no compulsory arguments)
    @staticmethod
    def print_greeting():
        """Performs a task related to the class but doesn't need instance or class data."""
        print("Welcome to the Animal Zoo!")

print("3. Class and Static Methods:")
Animal.print_greeting()

lion = Animal("Lion")
tiger = Animal("Tiger")

# Call Class method using the class
Animal.get_total_count()

# Call Static method using the instance
lion.print_greeting()
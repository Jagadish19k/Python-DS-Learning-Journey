# Python Practice File - inheritance

# 1. Single Inheritance
class Parent:  # Parent Class / Super Class
    name = "Sanyasi Rao"
    age = 65

    def get_parent_info(self):
        print(f"Parent name is {self.name} and age is {self.age}")

class Child(Parent):  # Child class / Subclass
    pass
    # The Child class inherits all attributes and methods from Parent

print("--- 1. Single Inheritance Example ---")
child_obj = Child()
child_obj.get_parent_info()
print(f"Child accessing Parent's attribute: {child_obj.name}")

print("-" * 30)

# 2. Single-Level Inheritance with super()
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Animal Name: {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        # Call the parent's constructor to initialize the 'name' attribute
        super().__init__(name)
        self.age = age

    # Method Overriding: Redefining the parent's show method
    def show(self):
        # You can call the parent's method from here too: super().show()
        print(f"Human Name: {self.name} and Age: {self.age}")

print("--- 2. Inheritance with super() and Overriding ---")
Person = Human("Jagadish", 25)
Person.show()

animal1 = Animal("Lion")
animal1.show()

print("-" * 30)

# 3. Multiple Inheritance
class LandAnimal:
    feature1 = "Can Walk"
    def move(self):
        print("Moving on land.")

class WaterAnimal:
    feature2 = "Can Swim"
    def move(self):
        print("Moving in water.")

class Amphibian(LandAnimal, WaterAnimal):
    """
    Inherits from both LandAnimal and WaterAnimal.
    Python follows MRO (Method Resolution Order): LandAnimal is checked first.
    """
    pass

print("--- 3. Multiple Inheritance Example ---")
frog = Amphibian()

# Accessing attributes from both parents
print(f"Amphibian feature: {frog.feature1}")
print(f"Amphibian feature: {frog.feature2}")

# Calling the 'move' method (will call LandAnimal.move due to MRO)
frog.move()

print(f"\nMethod Resolution Order (MRO): {Amphibian.__mro__}")
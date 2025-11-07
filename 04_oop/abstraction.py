# Python Practice File - abstraction
from abc import ABC, abstractmethod

# 1. Define an Abstract Base Class (ABC)
# Inheriting from ABC makes this class abstract.
class Vehicle(ABC):
    """
    An Abstract Base Class for different types of vehicles.
    It defines the blueprint for how a vehicle should behave.
    """
    
    # Define an Abstract Method
    @abstractmethod
    def move(self):
        """
        This method must be implemented by any concrete class
        that inherits from Vehicle.
        """
        pass
    
    # Define a Concrete Method (Non-abstract)
    def start_engine(self):
        """A common operation for all vehicles."""
        print("Engine started with a key.")

print("--- Abstract Class Example ---")

# 2. Define a Concrete Class
class Car(Vehicle):
    """
    A concrete class that provides an implementation for the abstract 'move' method.
    """
    def move(self):
        print("The car is driving on four wheels.")

class Boat(Vehicle):
    """
    Another concrete class implementing the abstract 'move' method differently.
    """
    def move(self):
        print("The boat is sailing on the water.")

print("-" * 20)

# 3. Demonstration

# You CANNOT instantiate the abstract class directly
try:
    # abstract_vehicle = Vehicle() 
    # This line would raise a TypeError: Can't instantiate abstract class Vehicle
    print("Cannot directly create an object of the abstract class 'Vehicle'.")
except TypeError as e:
    # This block will handle the expected error if the line above is uncommented
    pass 

# You CAN instantiate the concrete classes
my_car = Car()
my_boat = Boat()

print("\nCar operations:")
my_car.start_engine() # Call concrete method from abstract class
my_car.move()        # Call implemented abstract method

print("\nBoat operations:")
my_boat.start_engine()
my_boat.move()
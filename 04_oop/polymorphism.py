# Python Practice File - polymorphism

# 1. Method Overriding (Inheritance-based Polymorphism)
# Defining a common interface (method name) across a class hierarchy.

class Animal:
    """The base class defines a general behavior."""
    def show_voice(self):
        print("The animal makes a general sound.")

class Dog(Animal):
    """The subclass overrides the behavior."""
    def show_voice(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    """Another subclass overrides the behavior differently."""
    def show_voice(self):
        print("The cat meows: Meow.")

print("--- 1. Method Overriding Example ---")
animal_generic = Animal()
dog_instance = Dog()
cat_instance = Cat()

# The same method call (show_voice) behaves differently depending on the object type.
animal_generic.show_voice()
dog_instance.show_voice()
cat_instance.show_voice()

print("-" * 30)

# 2. Duck Typing (Behavioral Polymorphism)
# If it walks like a duck and quacks like a duck, it's a duck.
# Python focuses on *what an object can do*, not *what an object is*.

class Plane:
    def fly(self):
        print("The plane flies high in the sky.")

class Bird:
    def fly(self):
        print("The bird flies using its wings.")

class Man:
    def fly(self):
        print("The man is flying in a flight simulator.")
        
# A function that is NOT concerned with the object's type, only that it has a 'fly' method.
def let_it_fly(thing):
    thing.fly()

print("--- 2. Duck Typing Example ---")

# The same function call works for different, unrelated classes,
# because all objects share the 'fly' method signature.
pilot = Plane()
sparrow = Bird()
gamer = Man()

let_it_fly(pilot)
let_it_fly(sparrow)
let_it_fly(gamer)
# Python Practice File - functions_intro

# 1. Basic Function Definition and Call
def greet_user(name):
    """A function that takes a name and prints a greeting."""
    print(f"Hello, {name}! Welcome to Python practice.")

print("--- Basic Function Call ---")
greet_user("Jagadish")


# 2. Function with Return Value
def addition(a, b):
    """A function that returns the sum of two numbers."""
    return a + b

print("\n--- Function with Return ---")
result = addition(12, 12)
print(f"The result of addition(12, 12) is: {result}")


# 3. Function with Default Parameters
def calculate_area(length, width=1):
    """Calculates area. If width is not provided, defaults to 1."""
    return length * width

print("\n--- Function with Default Parameter ---")
area1 = calculate_area(10)          # Uses default width=1
area2 = calculate_area(10, 5)       # Uses provided width=5
print(f"Area with length=10, default width: {area1}")
print(f"Area with length=10, width=5: {area2}")


# 4. Function with Keyword Arguments (Keyword = Positional)
def display_details(name, age):
    """A function demonstrating flexible argument passing."""
    print(f"\nName: {name}, Age: {age}")

print("\n--- Function with Keyword Arguments ---")
# Positional call
display_details("Sanyasi Rao", 65)
# Keyword call (order doesn't matter)
display_details(age=34, name="Kalyan")
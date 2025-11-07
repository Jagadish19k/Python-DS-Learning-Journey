# Python Practice File - decorators

# 1. Basic Decorator with Fixed Arguments
# Define the decorator function
def log_decorator(func):
    """A decorator that wraps a function and adds simple logging."""
    def wrapper(a, b):
        print("--- DECORATOR: Starting execution of function ---")
        func(a, b)
        print("--- DECORATOR: Function execution complete ---")
    return wrapper

# Apply the decorator to the target function
@log_decorator
def addition(a, b):
    print(f"Total calculated by addition function: {a + b}")

print("Running Basic Decorator Example:")
addition(12, 45)

print("-" * 40)

# 2. Decorator with *args and **kwargs (More Flexible)
# This is a general pattern that works for functions with any number of arguments.
def flexible_decorator(func):
    """A decorator that can handle any number of positional or keyword arguments."""
    def wrapper(*args, **kwargs):
        print("--- FLEX DECORATOR: Preparing to call function ---")
        print(f"Arguments passed: {args}, Keywords passed: {kwargs}")
        
        # Call the original function with all its arguments
        func(*args, **kwargs)
        
        print("--- FLEX DECORATOR: Cleanup after function call ---")
    return wrapper

@flexible_decorator
def print_args(*args):
    print(f"Function received the following data: {args}")

print("Running Flexible Decorator Example:")
print_args(3234, 3, 4, name="user_data", version=1.0)
# Python Practice File - args_kwargs

# 1. *args (Arbitrary Positional Arguments)
# Allows a function to accept any number of positional arguments.
def sum_all(*args):
    """Calculates the sum of all passed positional arguments."""
    print(f"Received positional arguments: {args}")
    total = 0
    for num in args:
        total += num
    print(f"The sum is: {total}")

print("--- *args Example ---")
sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)


# 2. **kwargs (Arbitrary Keyword Arguments)
# Allows a function to accept any number of keyword arguments (passed as a dictionary).
def print_info(**kwargs):
    """Prints information passed as keyword arguments."""
    print(f"\nReceived keyword arguments: {kwargs}")
    print("User Info:")
    for key, value in kwargs.items():
        print(f" - {key.capitalize()}: {value}")

print("\n--- **kwargs Example ---")
print_info(name="Jagadish", age=25, city="Vizag")
print_info(product="Laptop", price=1200, warranty="3 years")


# 3. Combining *args and **kwargs
def combined_example(required_arg, *args, **kwargs):
    """Demonstrates a mix of required, positional, and keyword arguments."""
    print(f"\n--- Combined Example ---")
    print(f"Required Argument: {required_arg}")
    print(f"Additional Positional Arguments (*args): {args}")
    print(f"Keyword Arguments (**kwargs): {kwargs}")

combined_example("Start", 
                 10, 20, 30, # These go to *args
                 version=3.10, 
                 status="Active" # These go to **kwargs
                )
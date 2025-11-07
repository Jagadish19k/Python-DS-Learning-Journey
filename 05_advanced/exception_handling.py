# Python Practice File - exception_handling

# 1. Basic try-except (Handling DivisionByZero)
def safe_divide():
    print("--- 1. Basic try-except ---")
    try:
        # Code that might cause an error
        numerator = 10
        denominator = int(input("Enter a number to divide 10 by: "))
        result = numerator / denominator
    except ZeroDivisionError:
        # Code to handle the specific error
        print("Error: Cannot divide by zero. Please try again.")
    except ValueError:
        # Handle cases where input is not a valid integer
        print("Error: Invalid input. Please enter a whole number.")
    else:
        # Code that runs ONLY if no exceptions were raised in the try block
        print(f"Result: {result}")
    finally:
        # Code that runs regardless of whether an exception occurred
        print("Division attempt completed.")

safe_divide()

print("-" * 30)

# 2. try-finally (Ensuring cleanup code runs)
def file_operation():
    print("--- 2. try-finally (Cleanup) ---")
    file = None
    try:
        # Simulate opening a file
        file = open("temp_log.txt", "w")
        file.write("Writing some data...")
        # Simulate an error after writing
        # x = 1 / 0
    except ZeroDivisionError:
        print("Handled an unexpected division error.")
    finally:
        # Ensures the file is closed, even if an error occurred above
        if file:
            file.close()
            print("File handle successfully closed.")

file_operation()

print("-" * 30)

# 3. Raising Custom Exceptions
class InvalidAgeError(Exception):
    """Custom exception raised for invalid age input."""
    pass

def check_age(age):
    print("--- 3. Raising Custom Exceptions ---")
    if age < 0:
        # Raise an instance of the custom exception
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 150:
        raise InvalidAgeError("Age seems impossibly high.")
    else:
        print(f"Age {age} is valid.")

# Catching the custom exception
try:
    check_age(25)
    check_age(-5)
except InvalidAgeError as e:
    print(f"Caught Custom Error: {e}")
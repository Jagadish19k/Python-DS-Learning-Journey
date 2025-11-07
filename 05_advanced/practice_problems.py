# Python Practice File - practice_problems

# 1. Fibonacci Sequence Generator
def fibonacci(n):
    """Generates the first n numbers of the Fibonacci sequence."""
    a, b = 0, 1
    sequence = []
    print("\n--- 1. Fibonacci Sequence ---")
    if n <= 0:
        return []
    if n >= 1:
        sequence.append(a)
    if n >= 2:
        sequence.append(b)
        
    for _ in range(2, n):
        next_val = a + b
        sequence.append(next_val)
        a, b = b, next_val
    return sequence

print(f"Fibonacci (n=8): {fibonacci(8)}")
print("-" * 30)


# 2. Prime Number Checker
def is_prime(num):
    """Checks if a given number is a prime number."""
    print(f"\n--- 2. Prime Number Check ---")
    if num <= 1:
        return False
    # Check for factors from 2 up to the square root of the number
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 25 prime? {is_prime(25)}")
print("-" * 30)


# 3. String Palindrome Checker
def is_palindrome(text):
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""
    print(f"\n--- 3. Palindrome Check ---")
    # Clean the text: convert to lowercase and remove spaces
    cleaned_text = "".join(c.lower() for c in text if c.isalnum())
    return cleaned_text == cleaned_text[::-1]

print(f"Is 'Madam' a palindrome? {is_palindrome('Madam')}")
print(f"Is 'Python' a palindrome? {is_palindrome('Python')}")
print("-" * 30)


# 4. List Element Frequency Counter
def count_frequency(data_list):
    """Uses a dictionary to count the frequency of each element in a list."""
    print(f"\n--- 4. List Frequency Counter ---")
    frequency = {}
    for item in data_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

numbers = [1, 2, 2, 3, 4, 1, 5, 2, 6, 77, 77]
print(f"List: {numbers}")
print(f"Frequency: {count_frequency(numbers)}")
print("-" * 30)


# 5. Simple Class and Object Interaction
class Circle:
    """A class to represent a circle and calculate its area."""
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.PI * self.radius * self.radius

print("\n--- 5. Simple Class Problem ---")
circle1 = Circle(radius=5)
print(f"Circle with radius 5 has area: {circle1.calculate_area()}")

circle2 = Circle(radius=10)
print(f"Circle with radius 10 has area: {circle2.calculate_area()}")
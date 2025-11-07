# Python Practice File - comprehensions

# 1. List Comprehension
# Create a list of even numbers from 1 to 20
l_even = [i for i in range(1, 21) if i % 2 == 0]
print(f"List of even numbers (1-20): {l_even}")

# Create a list of squares of odd numbers from 1 to 10
l_squares_odd = [i**2 for i in range(1, 11) if i % 2 != 0]
print(f"List of squares of odd numbers (1-10): {l_squares_odd}")

# Simple transformation (upper-casing strings)
words = ["hello", "world", "python"]
l_upper = [word.upper() for word in words]
print(f"List of uppercase words: {l_upper}")

print("-" * 20)

# 2. Dictionary Comprehension
# Create a dictionary where keys are numbers (1-9) and values are their squares
d_comp_squares = {i: i**2 for i in range(1, 10)}
print(f"Dictionary of number-to-square: {d_comp_squares}")

# Create a dictionary filtering a list of tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
d_from_pairs = {k: v for k, v in pairs if v > 1}
print(f"Dictionary filtered from pairs: {d_from_pairs}")

# Using two iterables to create a dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
d_zip = {k: v for k, v in zip(keys, values)}
print(f"Dictionary from zipping two lists: {d_zip}")
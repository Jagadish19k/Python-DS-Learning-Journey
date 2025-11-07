# Python Practice File - lambda_map_filter

# 1. Lambda Functions (Anonymous Functions)

# Simple lambda function for addition
addition_lambda = lambda a, b: a + b
print("--- 1. Lambda Examples ---")
print(f"Lambda addition (32 + 23): {addition_lambda(32, 23)}")

# Lambda function for conditional checking
checker_lambda = lambda a: "even" if a % 2 == 0 else "odd"
print(f"Lambda checker (3 is): {checker_lambda(3)}")
print(f"Lambda checker (4 is): {checker_lambda(4)}")

print("-" * 30)

# 2. map() Function
# Applies a given function (lambda or def) to every item in an iterable.
a_map = [1, 2, 3, 4, 5]

# Using map with a lambda function to double every element
result_map_lambda = map(lambda x: x * 2, a_map)
print("--- 2. map() Example ---")
print(f"Original list: {a_map}")
print(f"Mapped (doubled) list: {list(result_map_lambda)}")

# Using map with a defined function
def triple(x):
    return x * 3

result_map_def = map(triple, a_map)
print(f"Mapped (tripled) list: {list(result_map_def)}")

print("-" * 30)

# 3. filter() Function
# Constructs an iterator from elements of an iterable for which a function returns True.
a_filter = [33, 34, 3, 343, 5, 36, 45656]

# Using a lambda function to filter out even numbers
result_filter_lambda = filter(lambda x: x % 2 == 0, a_filter)
print("--- 3. filter() Example ---")
print(f"Original list: {a_filter}")
print(f"Filtered (even numbers): {list(result_filter_lambda)}")

# Using a defined function to filter out small numbers
def is_large(x):
    return x > 100

result_filter_def = filter(is_large, a_filter)
print(f"Filtered (numbers > 100): {list(result_filter_def)}")
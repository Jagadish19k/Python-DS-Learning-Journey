# Python Practice File - variables_and_types

# Variable Creation with different data types
Number_ = 12             # int
String_ = "Jagadish Kumar" # str
Decimal_ = 12.34         # float
Complex_ = 45j           # complex
Boolean_ = False         # bool

# Print the type of each variable
print(f"Number_ type: {type(Number_)}")
print(f"String_ type: {type(String_)}")
print(f"Decimal_ type: {type(Decimal_)}")
print(f"Complex_ type: {type(Complex_)}")
print(f"Boolean_ type: {type(Boolean_)}")

print("-" * 20)

# Explicit Type Conversions

# Convert float to int (truncates the decimal part)
print(f"Type converting Decimal_ ({Decimal_}) to int: {int(Decimal_)}")
print(f"New type: {type(int(Decimal_))}")

# Convert boolean to int (False is 0, True is 1)
print(f"Type converting Boolean_ ({Boolean_}) to int: {int(Boolean_)}")

# Convert int to float
print(f"Type converting Number_ ({Number_}) to float: {float(Number_)}")
print(f"New type: {type(float(Number_))}")

print("-" * 20)

# String Slicing Examples
# [start:stop:step]

# Full string with step 1
print(f"Original string: {String_}")
print(f"Full slice (default): {String_[0::1]}")

# Reverse the string (step -1)
print(f"Reverse slice: {String_[::-1]}")
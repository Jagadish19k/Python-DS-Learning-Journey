# Python Practice File - operators

# Arithmetic Operators
a = 10
b = 3
print(f"a + b (Addition): {a + b}")
print(f"a - b (Subtraction): {a - b}")
print(f"a * b (Multiplication): {a * b}")
print(f"a / b (Division): {a / b}")
print(f"a % b (Modulus): {a % b}")
print(f"a ** b (Exponentiation): {a ** b}")
print(f"a // b (Floor Division): {a // b}")
print("-" * 20)


# Assignment Operators
x = 5
print(f"Initial x: {x}")
x += 2  # x = x + 2
print(f"x after += 2: {x}")
x *= 3  # x = x * 3
print(f"x after *= 3: {x}")
x //= 4 # x = x // 4
print(f"x after //= 4: {x}")
print("-" * 20)


# Comparison Operators
c = 7
d = 12
print(f"c == d: {c == d}")
print(f"c != d: {c != d}")
print(f"c > d: {c > d}")
print(f"c < d: {c < d}")
print(f"c >= 7: {c >= 7}")
print(f"d <= 12: {d <= 12}")
print("-" * 20)


# Logical Operators
p = True
q = False
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not q: {not q}")
print("-" * 20)


# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list3: {list1 is list3}")  # True (same object in memory)
print(f"list1 is list2: {list1 is list2}")  # False (different objects, even if content is the same)
print("-" * 20)


# Membership Operators
my_list = [10, 20, 30, 40]
print(f"10 in my_list: {10 in my_list}")
print(f"50 not in my_list: {50 not in my_list}")
print("-" * 20)


# Bitwise Operators (Simple Example)
# 6 is 0110 in binary, 3 is 0011
num1 = 6
num2 = 3
print(f"num1 & num2 (AND): {num1 & num2}")
print(f"num1 | num2 (OR): {num1 | num2}")
print(f"num1 ^ num2 (XOR): {num1 ^ num2}")
print(f"~num1 (NOT): {~num1}")
print(f"num1 << 1 (Left Shift): {num1 << 1}")
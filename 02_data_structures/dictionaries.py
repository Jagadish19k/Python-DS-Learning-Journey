# Python Practice File - dictionaries

# Dictionary Creation, CRUD operations
d = {10: 100, 20: 200, 30: 300, 40: 400}
print("Initial Dictionary:", d)

# Create/Update (C/U)
d[50] = 500  # Add a new key-value pair
print("After adding 50:500:", d)
d[50] = 600  # Update the value for key 50
print("After updating 50:600:", d)

# Delete (D)
del d[50]
print("After deleting key 50:", d)

print("-" * 20)

# Traversing
print("Traversing dictionary values:")
for i in d.values():
    print(i)

# Dictionary Methods
e2 = d.get(10)
print(f"\nValue for key 10 using get(): {e2}")
print(f"All values: {d.values()}")
print(f"All keys: {d.keys()}")
print(f"All items: {d.items()}")
print(f"Pop item (removes last inserted): {d.popitem()}")
print(f"Dictionary after popitem(): {d}")

# Merging Dictionaries (Manual Update)
d1 = {50: 500, 60: 600, 70: 700}
for i in d1:
    d[i] = d1[i]
print(f"\nDictionary after merging d1: {d}")

# Sum of Dictionary Values
sum_d = 0
for i in d:
    sum_d += d[i]
print(f"Sum of all dictionary values: {sum_d}")

# Application: Frequency Counter
freq = [1, 1, 1, 1, 2, 2, 2, 4, 5, 6, 77, 77, 77]
d_freq = {}

for i in freq:
    if i in d_freq.keys():
        d_freq[i] += 1
    else:
        d_freq[i] = 1

print(f"\nFrequency of elements in the list: {d_freq}")
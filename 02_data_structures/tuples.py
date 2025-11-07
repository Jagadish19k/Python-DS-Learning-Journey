# Python Practice File - tuples

# Tuple Creation
a = (1, 2, 2, 3, 4, 5)
print(f"Original Tuple: {a}")

# Traversing/Iterating
print("\nTraversing the tuple:")
for i in range(len(a)):
    print(a[i])

# Tuple Functions
index_of_5 = a.index(5)
print(f"\nIndex of element 5: {index_of_5}")

counts_of_2 = a.count(2)
print(f"Count of element 2: {counts_of_2}")

# Tuple Unpacking
q, w, e, r = (1, 2, 3, 4)
print(f"\nUnpacked variables:")
print(f"q: {q}")
print(f"r: {r}")
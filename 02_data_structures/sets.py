# Python Practice File - sets

# Set creation (Note: duplicates are automatically removed and order is not guaranteed)
s = {1, 2, 3, 4, 5, 5, 4, 3}
print(f"Initial set (duplicates removed): {s}")

# Add elements
s.add(6)
print(f"After adding 6: {s}")

# Remove elements
s.remove(6)
print(f"After removing 6: {s}")

# Discard element (safer than remove as it doesn't raise an error if the element is not found)
s.discard(1)
s.discard(100)
print(f"After discarding 1: {s}")

# Pop element (removes a random element from the set)
popped_element = s.pop()
print(f"Popped element: {popped_element}")
print(f"Set after pop: {s}")

# Clear set
s_clear = {1, 2}
s_clear.clear()
print(f"Set after clear: {s_clear}")

print("-" * 20)

# Set Mathematical Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Set A: {A}")
print(f"Set B: {B}")

# Union (all elements in either set)
print(f"Union (A | B): {A.union(B)}")

# Intersection (common elements)
print(f"Intersection (A & B): {A.intersection(B)}")

# Difference (elements in A but not in B)
print(f"Difference (A - B): {A.difference(B)}")

# Symmetric Difference (elements in either set, but not in both)
print(f"Symmetric Difference (A ^ B): {A.symmetric_difference(B)}")
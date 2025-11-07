# Python Practice File - lists

# List for positive/negative number separation
Lits_totry = [323, 435, -43, -43, -67, -23, 6775, 99999]
postive_num = []
Negative_num = []

for i in Lits_totry:
    if i >= 0:
        postive_num.append(i)
    else:
        Negative_num.append(i)
        
print(f"Original List: {Lits_totry}")
print(f"Positive numbers: {postive_num}")
print(f"Negative numbers: {Negative_num}")

print("-" * 20)

# List Mean Calculation
List_of_Values = [233, 56, 67, 89, 554, 345]
sum_val = 0
for i in List_of_Values:
    sum_val += i
    
Mean_val = (sum_val // len(List_of_Values))
print(f"List for Mean calculation: {List_of_Values}")
print(f"The average Value (integer division) of the list is: {Mean_val}")

print("-" * 20)

# Finding Largest Element
largest = List_of_Values[0]
index = 0

for i in range(len(List_of_Values)):
    if List_of_Values[i] > largest:
        largest = List_of_Values[i]
        index = i
        
print(f"The largest number is {largest} at index {index}")

print("-" * 20)

# Finding First and Second Largest Element
List_for_largest = [233, 56, 67, 89, 554, 345]
first_largest = List_for_largest[0]
Secound_largest = List_for_largest[0]

for i in List_for_largest:
    if i > first_largest:
        Secound_largest = first_largest
        first_largest = i
    elif i > Secound_largest:
        Secound_largest = i

print(f"List for Largest check: {List_for_largest}")
print(f"Second largest: {Secound_largest}, First largest: {first_largest}")

print("-" * 20)

# Check if List is Sorted
sorted_or_not = [1, 2, 3, 6, 5]
print(f"Checking if list {sorted_or_not} is sorted:")

for i in range(len(sorted_or_not) - 1):
    if sorted_or_not[i] < sorted_or_not[i+1]:
        continue
    else:
        print("Your list is NOT sorted")
        break
else:
    print("Your list IS sorted")

# Example of a sorted list check
sorted_example = [1, 2, 3, 4, 5]
print(f"\nChecking if list {sorted_example} is sorted:")
for i in range(len(sorted_example) - 1):
    if sorted_example[i] < sorted_example[i+1]:
        continue
    else:
        print("Your list is NOT sorted")
        break
else:
    print("Your list IS sorted")
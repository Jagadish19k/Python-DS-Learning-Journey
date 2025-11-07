# Python Practice File - conditionals_loops

# Conditionals (if, elif, else)
Ammo = 31
if Ammo > 0:
    print("Fire...!")
elif Ammo < 30:
    print("Ammo there but need full mazine reload")
else:
    print("Please Reload the gun")

# For Loop (Counting Down)
print("\nCounting down with a for loop:")
for i in range(10, 0, -1):
    print(i)

# For Loop (Multiplication Table)
n_table = int(input("\nPlease Enter Value of table: "))
print(f"Printing table for {n_table}:")
for i in range(n_table, n_table * 10 + 1, n_table):
    print(f"{i}")

# For Loop (Iterating over a String)
Name = "Jagadish is learning python"
print("\nIterating over a string:")
for i in range(len(Name)):
    print(Name[i])

# Loop Control (break)
Skip_Num = 23
print("\nUsing break:")
for i in range(1, 26):
    if (i == Skip_Num):
        break
    else:
        print(i)

# Loop Control (continue)
print("\nUsing continue:")
for i in range(1, 26):
    if (i == Skip_Num):
        continue
    print(i)

# Loop Application (Sum of N numbers)
sum_of_n = 0
n_sum = int(input("\nPlease enter the N NUMBER to print SUM of N: "))
for i in range(1, n_sum + 1):
    sum_of_n += i
print(f"The sum of numbers up to {n_sum} is: {sum_of_n}")

# Loop Application (Factorial)
fact = 1
n_fact = int(input("\nPlease enter the N NUMBER to print Factorial: "))
for i in range(1, n_fact + 1):
    fact *= i
print(f"The factorial of {n_fact} is: {fact}")

# Loop Application (Prime Check)
n_prime = int(input("\nPlease Enter Number to check weather it's a prime or not: "))
count = 0
for i in range(1, n_prime + 1):
    if n_prime % i == 0:
        count += 1
if count == 2:
    print(f"{n_prime} is a prime number")
else:
    print(f"{n_prime} is not a prime number")

# While Loop (Digit Separation)
Num = int(input("\nEnter number to spearate and print in anew line: "))
print("Separated digits:")
while Num > 0:
    print(Num % 10)
    Num //= 10

# While Loop (Reverse Number)
rev = 0
Num_rev = int(input("\nEnter number to reverse: "))
Original_Num_rev = Num_rev
while Num_rev > 0:
    rev = rev * 10 + Num_rev % 10
    Num_rev //= 10
print(f"The reverse of {Original_Num_rev} is: {rev}")
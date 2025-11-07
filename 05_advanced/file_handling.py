# Python Practice File - file_handling

FILE_NAME = "sample_data.txt"

# 1. Writing to a File (using 'w' mode)
# 'w' mode overwrites the file if it exists.
# We use 'with open' to ensure the file is automatically closed.
print("--- 1. Writing to a File (w) ---")
try:
    with open(FILE_NAME, 'w') as file:
        file.write("First line of new content.\n")
        file.write("Second line, which is written right after the first.\n")
        file.write("Data science requires clean file handling!\n")
    print(f"Successfully wrote content to {FILE_NAME}.")
except Exception as e:
    print(f"An error occurred during writing: {e}")

print("-" * 30)

# 2. Reading from a File (using 'r' mode)
print("--- 2. Reading Entire File (r) ---")
try:
    with open(FILE_NAME, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file {FILE_NAME} was not found.")

print("-" * 30)

# 3. Reading Line by Line (using readline() and readlines())
print("--- 3. Reading Line by Line ---")
try:
    # Read a single line
    with open(FILE_NAME, 'r') as file:
        first_line = file.readline()
        print(f"First line (readline()): {first_line.strip()}") # Use strip() to remove trailing newline

    # Read all lines into a list
    with open(FILE_NAME, 'r') as file:
        all_lines = file.readlines()
        print(f"Total lines read (readlines()): {len(all_lines)}")
        print(f"Content of line 3: {all_lines[2].strip()}")
except Exception as e:
    print(f"An error occurred during line reading: {e}")

print("-" * 30)

# 4. Appending to a File (using 'a' mode)
# 'a' mode adds new content to the end of the file.
print("--- 4. Appending to a File (a) ---")
try:
    with open(FILE_NAME, 'a') as file:
        file.write("Appended line 4 at the end.\n")
        file.write("Another appended line 5.\n")
    print(f"Successfully appended content to {FILE_NAME}.")
except Exception as e:
    print(f"An error occurred during appending: {e}")

# 5. Final Read to confirm append
print("\n--- 5. Final Read to Confirm Append ---")
with open(FILE_NAME, 'r') as file:
    print(file.read())
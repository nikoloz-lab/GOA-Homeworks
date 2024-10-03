# 1. Explain what .upper() is via comments.
# The .upper() method converts all characters in a string to uppercase letters.
example_string = "Hello World"
print(example_string.upper())  # Output: "HELLO WORLD"

# 2. Explain what .lower() is via comments.
# The .lower() method converts all characters in a string to lowercase letters.
example_string = "Hello World"
print(example_string.lower())  # Output: "hello world"

# 3. Store the string in capital letters in a variable, then use the .capitalize() function
# to convert the first letter to a capital letter.
capital_string = "HELLO WORLD"
print(capital_string.capitalize())  # Output: "Hello world"
# Notice that the .capitalize() method converts only the first letter to uppercase and 
# makes the rest of the string lowercase.

# 4. Enter the client's first and last name separately, then convert the name to lowercase,
# add the last name, and print.
first_name = input("Enter the first name: ").lower()
last_name = input("Enter the last name: ")
full_name = first_name + " " + last_name
print("Client's full name: ", full_name)  # Example output: "john Smith"

# 5. Create a variable name='goalorienteacademy', then use the .find() function to find specific characters:
name = "goalorienteacademy"

# .find() method returns the index of the first occurrence of the substring or -1 if not found.
index_o = name.find('o')  # Finds the first 'o'
index_a = name.find('a')  # Finds the first 'a'
index_y = name.find('y')  # Finds the first 'y'
index_x = name.find('x')  # Since 'x' does not exist, it returns -1

# Printing the results
print("First occurrence of 'o':", index_o)  # Output: 1
print("First occurrence of 'a':", index_a)  # Output: 4
print("First occurrence of 'y':", index_y)  # Output: 15
print("First occurrence of 'x':", index_x)  # Output: -1
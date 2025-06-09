# Creating a string
s = "Hello, Python World!"

# Basic Info
print(len(s))               # Length of the string
print(str(123))             # Convert number to string

# Changing Case
print(s.lower())            # All lowercase
print(s.upper())            # All uppercase
print(s.capitalize())       # Capitalize first letter
print(s.title())            # Title Case (First letter of each word capitalized)
print(s.swapcase())         # Swap upper to lower and vice versa

# Searching
print(s.find("Python"))     # First index of substring or -1
print(s.rfind("o"))         # Last index of substring
print(s.index("World"))     # Same as find, but error if not found
print(s.count("o"))         # Count how many times a character appears

# Checking Content
print(s.endswith("d!"))     # True if it ends with the given characters(Case sensitive)
print(s.startswith("Hell")) # True if it starts with the given characters(Case sensitive)
print(s.isalpha())          # True if all characters are letters
print(s.isdigit())          # True if all characters are digits
print(s.isalnum())          # True if all characters are letters or digits
print(s.islower())          # True if all letters are lowercase
print(s.isupper())          # True if all letters are uppercase
print(s.isspace())          # True if all characters are whitespace
print(s.istitle())          # True if title case

# Modifying Content
print(s.strip())            # Remove spaces from both ends
print(s.lstrip())           # Remove spaces from the left
print(s.rstrip())           # Remove spaces from the right
print(s.replace("Python", "Java"))  # Replace substring
print(s.split())            # Split by whitespace
print(s.split(","))         # Split by comma
print(s.rsplit(" ", 1))     # Split from right, once
print(",".join(["a", "b", "c"]))     # Join list with comma

# Formatting Strings
name = "Alice"
age = 19
print("My name is {} and I am {} years old.".format(name, age))  # old style
print(f"My name is {name} and I am {age} years old.")             # f-string (best)

# Escape sequences
print("Hello\nWorld")       # New line
print("Hello\tWorld")       # Tab
print("She said, \"Hi!\"")  # Escape quotes

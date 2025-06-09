# Creating a dictionary

my_dict = {
    "name": "Alice",
    "age": 19,
    "city": "Mumbai"
}

# Accessing values
print(my_dict["name"])           # Output: Alice
print(my_dict.get("age"))        # Output: 19
print(my_dict.get("email", "N/A"))  # Output: N/A (if key not found) 

# Adding and updating values
my_dict["email"] = "alice@example.com"   # Add new key
my_dict["age"] = 20                      # Update existing key
print(my_dict)

# Removing values
my_dict.pop("city")             # Removes 'city'
print(my_dict)

del my_dict["email"]            # Deletes key
print(my_dict)

# Clear all values
copy_dict = my_dict.copy()      # Make a copy
my_dict.clear()                 # Clear all items
print(my_dict)                  # {}

# Dictionary info
print(len(copy_dict))           # Output: 2
print(copy_dict.keys())         # dict_keys(['name', 'age'])
print(copy_dict.values())       # dict_values(['Alice', 20])
print(copy_dict.items())        # dict_items([('name', 'Alice'), ('age', 20)])


# Looping
for key in copy_dict:
    print(key, copy_dict[key])  # key + value

# Using update()
copy_dict.update({"city": "Delhi", "age": 21})
print(copy_dict)

# Check if key exists
print("name" in copy_dict)      # Output: True
print("phone" in copy_dict)     # Output: False

# Create dictionary from list of tuples
pairs = [("a", 1), ("b", 2)]
new_dict = dict(pairs)
print(new_dict)                 # {'a': 1, 'b': 2}

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)                  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# To input the same value for all keys
key = ["x","y","z"]
key_dict = dict.fromkeys(key,1)
print(key_dict)

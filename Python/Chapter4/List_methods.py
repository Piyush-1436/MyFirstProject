# Create a list
my_list = [10, 20, 30, 40]

# 1. Add items
my_list.append(50)             # Adds 50 at the end
print(my_list)                 # [10, 20, 30, 40, 50]

my_list.insert(2, 25)          # Inserts 25 at index 2
print(my_list)                 # [10, 20, 25, 30, 40, 50]

my_list.extend([60, 70])       # Adds multiple items
print(my_list)                 # [10, 20, 25, 30, 40, 50, 60, 70]

# 2. Remove items
my_list.remove(25)             # Removes first occurrence of 25
print(my_list)                 # [10, 20, 30, 40, 50, 60, 70]

my_list.pop()                  # Removes last item
print(my_list)                 # [10, 20, 30, 40, 50, 60]

my_list.pop(1)                 # Removes item at index 1
print(my_list)                 # [10, 30, 40, 50, 60]

# 3. Get info
print(my_list.index(50))      # Output: 3 (index of 50)
print(my_list.count(30))      # Output: 1 (30 appears once)

# 4. Sorting and reversing
my_list.sort()                 # Sorts in ascending order
print(my_list)                 # [10, 30, 40, 50, 60]

my_list.sort(reverse=True)     # Sorts in descending order
print(my_list)                 # [60, 50, 40, 30, 10]

my_list.reverse()              # Reverses the list
print(my_list)                 # [10, 30, 40, 50, 60]

# 5. Copy and clear
new_list = my_list.copy()      # Makes a copy of the list
print(new_list)                # [10, 30, 40, 50, 60]

my_list.clear()                # Removes all items
print(my_list)                 # []

# 6. Some useful functions
numbers = [5, 10]()
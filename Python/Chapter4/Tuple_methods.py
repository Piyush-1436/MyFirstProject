my_tuple = (10, 20, 30, 20, 40)

# Tuple methods
print(my_tuple.count(20))   # 2
print(my_tuple.index(30))   # 2

# Accessing
print(my_tuple[0])          # 10
print(my_tuple[-1])         # 40
print(my_tuple[1:4])        # (20, 30, 20)

# Loop
for item in my_tuple:
    print(item)

# Nested tuple
nested = (1, (2, 3), 4)
print(nested[1][0])         # 2

# Convert list to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)             # (1, 2, 3)

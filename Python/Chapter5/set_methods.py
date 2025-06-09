# Creating sets
my_set = {1, 2, 3}
another_set = {3, 4, 5}

# Basic methods
my_set.add(4)               # Adds an element
my_set.remove(2)            # Removes an element (error if not present)
my_set.discard(10)          # Removes if present (no error if not)
my_set.pop()                # Removes a random element
my_set.clear()              # Removes all elements

# Set operations
union_set = my_set.union(another_set)          # Combines sets
intersection_set = my_set.intersection(another_set)  # Common elements
difference_set = my_set.difference(another_set)      # Items in my_set not in another_set
symmetric_diff = my_set.symmetric_difference(another_set)  # Elements in either, but not both

# Update methods (modify the set in place)
my_set.update(another_set)                     # Adds all elements from another_set
my_set.intersection_update(another_set)        # Keeps only common elements
my_set.difference_update(another_set)          # Removes elements found in another_set
my_set.symmetric_difference_update(another_set)  # Keeps only elements in one of the sets

# Check relationships
my_set.issubset(another_set)     # True if all elements of my_set are in another_set
my_set.issuperset(another_set)   # True if my_set contains all elements of another_set
my_set.isdisjoint(another_set)   # True if sets have no elements in common

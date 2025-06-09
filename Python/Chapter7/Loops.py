#  The are 2 types of loops
# for loop & while loop (they perfrom the same task in ) different way
# while (condition): The block keeps executing until the condition is true 

# 🔁 Python Loops – All-in-One Notes

# ✅ range() function
# Used in for loops to generate a sequence of numbers
# range(stop)               # 0 to stop-1
# range(start, stop)        # start to stop-1
# range(start, stop, step)  # with step (can be negative)

# Examples:
for i in range(5):          # 0 to 4
    print(i)

for i in range(1, 6):       # 1 to 5
    print(i)

for i in range(10, 0, -1):  # 10 to 1 (reverse)
    print(i)

# 🔄 Loop Control Statements
# break: exits the loop
# continue: skips current iteration
# else: runs if loop completes without break

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished without break")

# 📦 Useful Functions with Loops

# enumerate() – get index + value
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip() – combine multiple lists
names = ['piyush', 'no one']
scores = [98, 96]
for name, score in zip(names, scores):
    print(name, score)

# len() – get number of items
fruits = ['apple', 'banana']
print(len(fruits))  # Output: 2

# 🔁 While Loop – Example
i = 1
while i <= 5:
    print(i)
    i += 1

# Create 4 variables:
# your_name (string)
# your_age (int)
# your_height (float)
# is_coding (bool)
# 👉 Print them all using a single print() with an f-string.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

answer = input("Is coding cool? (yes \ no)")
is_yes = bool(answer == "yes")

print(name)
print(age)
print(height)
print("User's answer is", is_yes)
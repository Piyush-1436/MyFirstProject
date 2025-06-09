# Write a python function which converts inches to centimeters.
def func(inch):
    return inch * (5/2)
n = int(input("Enter your number: "))
print(f"The value of the corresponding value in centimeters is {func(n)}")
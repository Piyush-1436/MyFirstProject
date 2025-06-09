# Write a program using functions to find greatest of three numbers.
def func():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    if (a>b and a>c):
        print(f"{a} is the greatest number of the other two ({b} and {c})")
    elif(b>a and b>c):
        print(f"{b} is the greatest number of the other two ({a} and {c})")
    elif(c>a and c>b):
        print(f"{c} is the greatest number of the other two ({b} and {a})")
func()
        
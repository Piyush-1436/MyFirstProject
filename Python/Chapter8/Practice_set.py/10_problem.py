# Write a python function to print multiplication table of a given number.
def func():
    n = int(input("Enter your number: "))
    for i in range(1,11):
        print(f"{n} X {10} = {n*i}")
func()
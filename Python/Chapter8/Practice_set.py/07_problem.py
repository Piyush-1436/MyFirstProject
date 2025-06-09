# # Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def func(n):
    if (n == 0):
        return
    print("*" * n)
    func(n-1)
func(3)
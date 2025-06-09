# Write a recursive function to calculate the sum of first n natural numbers.
def func():
    n = int(input("Enter your number: "))
    result = 0
    for i in range(0,n+1):
        result = result + i
    return (f"The sum of first {n} natural numbers is {result}")
a = func()
print(a)

#  OR
def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n
print(sum(10))
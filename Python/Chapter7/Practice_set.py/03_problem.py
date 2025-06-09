# # Write a program to print multiplication table of a given number using for loop.
a = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
    i += 1

# With while loop

c = 1
b = int(input("Enter your number:"))
while(c<11):
    print(f"{b} X {c} = {b*c}")
    c += 1
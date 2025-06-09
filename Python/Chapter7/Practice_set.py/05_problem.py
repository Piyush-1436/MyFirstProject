a = int(input("Enter your number:"))
for i in range(2,a):
    if(a%i==0):
        print(f"{a} is not a prime number.")
else:
    print(f"{a} is a prime number.")
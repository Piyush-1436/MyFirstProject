

# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
a = "Ex"
b = "A"
c = "B"
d = "C"
e = "D"
f = "F"
num1 = int(input("Enter your marks: "))
if (90<=num1<=100):
    print(f"Congratulations!,You got {a} grade.")
elif (80<=num1<90):
    print(f"Congratulations!,You got {b} grade.")
elif (70<=num1<80):
    print(f"Congratulations!,You got {c} grade.")
elif (60<=num1<70):
    print(f"Congratulations!,You got {d} grade.")
elif (50<=num1<60):
    print(f"Congratulations!,You got {e} grade.")
elif (num1<50):
    print(f"Congratulations!,You got {f} grade.")

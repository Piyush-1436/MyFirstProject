# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
# 
# Place these files in a folder for a 13 – year old.
def func():
    for n in range(2,21):
        print(f"Following is the multiplication table of {n}")
        with open(f"table/table_{n}.txt", "w") as f:
            for i in range(1,11):
                line = ((f"{n} X {i} = {n*i}"))
                print(line)
                f.write(line + "\n")

func()
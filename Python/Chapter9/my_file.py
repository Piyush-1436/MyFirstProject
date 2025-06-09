st = "Piyush, you  are amazing"

f = open("mefile.txt" , "w")

f.write(st)

f.close() 

# The same can be done using the with  statement :
with open("mefile.txt") as f:
    print(f.read())

# Now you dont have to close the file

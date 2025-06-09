# The random-access memory is volatile, and all its contents are lost once a program terminates. 
# In order to persist the data forever, we use files.
# A file is data stored in a storage device.
# A p

'''

There are 2 types of files:
1.Text files (.txt, .c, etc)
2.Binary files (.jpg, .dat, etc)

'''
#  Python File I/O – Full Notes

#  1. Opening a File
f = open("filename.txt", "mode")

# Modes:
# r = open for reading
# w = open for writing
# a = open for appending
# + = open for updating.
# ‘rb’= will open for read in binary mode.
# ‘rt’= will open for read in text mode.

# Examples
f = open("data.txt", "r")
f = open("data.txt", "w")
f = open("data.txt", "a")
f = open("data.txt", "rb")

#  2. Reading from a File
f = open("data.txt", "r")
print(f.read())         # Read whole file
print(f.read(5))        # Read first 5 chars
print(f.readline())     # Read one line
print(f.readlines())    # Read all lines as list
f.close()

#  3. Writing to a File
f = open("data.txt", "w")
f.write("This overwrites the file.")
f.close()

#  4. Appending to a File
f = open("data.txt", "a")
f.write("\nThis is added at the end.")
f.close()

#  5. Using 'with' (Auto-closes the file)
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

#  6. Checking, Creating, Deleting Files/Folders
import os

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists.")

# Delete file
os.remove("data.txt")

# Create folder
os.mkdir("myfolder")

# Delete folder (must be empty)
os.rmdir("myfolder")

#  7. Write Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("data.txt", "w") as f:
    f.writelines(lines)

#  Summary Table (as comment for quick revision)

# Task         | Code
# ------------ | ----------------------------
# Read all     | f.read()
# Read one line| f.readline()
# Read lines   | f.readlines()
# Write        | f.write("text")
# Append       | open(file, "a")
# Auto-close   | with open(...) as f:
# File exists  | os.path.exists("file")
# Delete file  | os.remove("file")
# Create folder| os.mkdir("folder")
# Delete folder| os.rmdir("folder")

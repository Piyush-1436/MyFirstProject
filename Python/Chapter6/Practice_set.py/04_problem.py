username = input("Enter your username:")
if (len(username)<=10):
    print(f"{username}, This username contain 10 or less than 10 characters.")
else:
    print(f"{username}, This username contain more than 10 characcters.")

# New program.

statement = input("Enter your statement: ")
if("caste" in statement):
    print("This comment is against the guidlines.Try again.")
else:
    print(statement)
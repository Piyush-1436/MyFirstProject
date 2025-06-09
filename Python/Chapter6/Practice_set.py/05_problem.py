l = ["Piyush","Jeet","Athu","Kartik"]
name = input("Enter your name: ")
if  (name in l):
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")

#  But what if someone uses 1st letter small, then to also make it work.

a = input("Enter your statement: ")
if ("Piyush".lower() in a.lower()):
    print(f"This post is about {a}")
else:
    print(f"This post is not about {a}")
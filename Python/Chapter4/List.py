object = ["Apple","Student",5,3.45,"Christmas"]
print(object[0])       # We cannot change the existing string but we can make a new string
                       # But  we can make changes in the list
object[0] = "Piyush"          
print(object)             # So unlike strings, list are mutable

object.append("Evening")  # Add the  characters at the end
print(object)

#  For example

l1 = [1,49,12,35,16,81] 
l1.reverse()             # Sort it in descending order
print(l1)
l1.insert(3,18)          # Insert any character at the desired index
print(l1)
l1.sort()                # Sort it in ascending order
print(l1)
l1.pop(5)                # Remove the desired index's character
print(l1)
def func(name , ending):
    print("Good Day Mr. " + name + " " + ending + " for coming on this ocassion.")
    return "Have a great night."   #This will be the info or value in the empty variable [a]
func("Piyush", "Thank you")
a = func("Piyush", "Thank you") # If the return is not used then a will contain no info and print "None"
print(a)
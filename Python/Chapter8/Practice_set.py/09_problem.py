# Write a python function to remove a given word from a list and strip it at the same time.
# IMPORTANT
l = ["Piyush","Ashish","Ansh","Jayesh","sh"]
def rem(l,word):
    n =[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
print(rem(l,"sh"))
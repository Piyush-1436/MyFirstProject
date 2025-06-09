Name = input("Enter your name: ")
date = "29/04/2025"
letter = '''
       Dear <|Name|>
       You are selected!
       <|Date|>
       '''
print(letter.replace("<|Name|>",Name).replace("<|Date|>",date))

# Replacing from the output

z = letter.replace("<|Name|>", "Punk").replace("<|Date|>","Don't care")
print(z)
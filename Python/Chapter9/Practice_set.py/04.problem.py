# A file contains a word “Donkey” multiple times. 
# You need to write a program which replace this word with ##### by updating the same file.
def func():
    with open("sample.txt") as f:
        content =f.read()
    if ("Donkey" in content):
        with open("sample.txt" , "w") as f:
            content = content.replace("Donkey", "#####")
            f.write(content)
            print("The word 'Donkey' is replaced by '#####' ")
    else:
        print("There is no such word as 'Donkey' in the content.")
func()
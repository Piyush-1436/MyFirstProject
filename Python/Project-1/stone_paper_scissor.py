import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice: ")
youDict = {"scissor": 1, "paper":-1, "stone":0}
if(youstr not in youDict):
    print("Invalid choice")

else:
    you = youDict[youstr]

    reverseDict = {1:"Scissor", -1 :"Paper", 0 :"Stone"}


    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if(computer == you):
        print("It's a draw.")


    else:
        if(computer == -1 and you == 1):
            print("You win!")
        if(computer == -1 and you == 0):
            print("You lose!")
        if(computer == 0 and you == -1):
            print("You win!")
        if(computer == 0 and you == 1):
            print("You lose!")
        if(computer == 1 and you == 0):
            print("You win!")
        if(computer == 1 and you == -1):
            print("You lose!")

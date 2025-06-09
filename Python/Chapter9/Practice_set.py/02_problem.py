# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing a game..")
    score = random.randint(1,63)  # Return a random integer range between [a,b]
    # Fetch the hi_score
    with open("hi_score.txt") as f:
        hi_score = f.read()
        if (hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    print(f"Your score is {score}")
    if (score>hi_score):
        with open("hi_score.txt" , "w") as f:
            f.write(str(score))
            print("New high score")

game()
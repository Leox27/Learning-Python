import random

def game():
    print("You are playing the game")
    score = random.randint(1, 62)       # For getting random integer

    # Fecth the hi-score
    with open("p2_Hi-Score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore) # For converting str to int
        else:
            hiscore = 0

    print(f"Your score:{score}")
    if(score > hiscore or hiscore == ""):

        # Wrie the hiscore to the file
        with open("p2_Hi-Score.txt", "w") as f:
            f.write(str(score))

    return score

game()
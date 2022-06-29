#Objective 7: Challenges
#Rock, paper, scissors challenge
def roll():
    import random
    Rolled = random.randint(1,3)
    if Rolled == 1:
        return "Rock"
    elif Rolled == 2:
        return "Paper"
    elif Rolled == 3:
        return "Scissors"
    else:
        return "Error"
computerScore = 0
playerScore = 0
print("Remember to use a capital at the start")
playerRoll = input("Enter Rock, Paper or Scissors:")
computerRoll = roll()
if computerRoll == "Rock":
    if playerRoll == "Rock":
        print("Draw")
    elif playerRoll == "Scissors":
        print("You lost")
        computerScore = computerScore + 1
    elif playerRoll == "Paper":
        print("You won")
        playerScore = playerScore + 1
    else:
        print("Error")
elif computerRoll == "Paper":
    if playerRoll == "Rock":
        print("You lost")
        computerScore = computerScore + 1
    elif playerRoll == "Scissors":
        print("You won")
        playerScore = playerScore + 1
    elif playerRoll == "Paper":
        print("Draw")
    else:
        print("Error")
elif computerRoll == "Scissors":
    if playerRoll == "Rock":
        print("You won")
        playerScore = playerScore + 1
    elif playerRoll == "Scissors":
        print("Draw")
    elif playerRoll == "Paper":
        print("You lost")
        computerScore = computerScore + 1
    else:
        print("Error")
else:
    print("Error")

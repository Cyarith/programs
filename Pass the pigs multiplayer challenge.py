#Objective 8: Challenges
#Pass the pigs challenge
def Roll():
    import random
    b = random.randint(1,20)
    return b
#Main program
PlayerScore1 = 0
PlayerScore2 = 0
HeldScore = 0
PigA = 0
PigB = 0
Player = 1 
while PlayerScore1 < 100 and PlayerScore2 < 100:
    print("It's Player",Player,"'s Turn")
    turn = input("")
    print("")
    if turn == "Pass" and Player == 1 or turn == "pass" and Player == 1:
        PlayerScore1 = PlayerScore1 + HeldScore
        Player = 2
        HeldScore = 0
        print("==================================")
    elif turn == "Pass" and Player == 2 or turn == "pass" and Player == 2:
        PlayerScore2 = PlayerScore2 + HeldScore
        Player = 1
        HeldScore = 0
        print("==================================")
    else:
        print("")
    PigA = Roll()
    PigB = Roll()
    if PigA == PigB and PigA == 2:
        print("Double Snouter + 20 points")
        HeldScore += 20
    elif PigA == PigB and PigA == 3:
        print("Doule Trotter + 20 points")
        HeldScore += 20
        HeldScore = HeldScore + 1
    elif PigB < 7 and PigB > 5 and PigA < 7 and PigA > 5:
        print("Sider + 1 point")
        HeldScore = HeldScore + 1
    elif PigB >= 7 and PigA >= 7 and PigB < 20 and PigA < 20:
        print("Sider + 1 point")
        HeldScore = HeldScore + 1
    elif PigA == 1 or PigB == 1:
        print("Trotter + 5 points")
        HeldScore = HeldScore + 5
    elif PigA == PigB and PigA == 1:
        print("Double Trotter + 20 points")
        HeldScore = HeldScore + 20
    elif PigA == 4 or PigB == 4:
        print("Snouter + 5 points")
        HeldScore = HeldScore + 5
    elif PigA == PigB and PigA == 4:
        print("Double Snouter + 20 points")
        HeldScore = HeldScore + 20
    elif PigA == 5 or PigB == 5:
        print("Razorback + 5 points")
        HeldScore = HeldScore + 5
    elif PigA == PigB and PigA == 5:
        print("Double Razorback + 20 points")
        HeldScore = HeldScore + 20
    else:
        print("Pig Out - Reset to 0")
        print("Turn is passed to the other player")
        print("==================================")
        HeldScore = 0
        if Player == 1:
            Player = 2
        elif Player == 2:
            Player = 1
        else:
            Print("Error")
    if Player == 1:
        print("Your Unbanked Score is",HeldScore)
        print("Your Banked Score is",PlayerScore1)
    elif Player == 2:
        print("Your Unbanked Score is",HeldScore)
        print("Your Banked Score is",PlayerScore2)
    else:
        print("Error")
if PlayerScore1 >= 100:
    print("Player 1 Wins!")
elif PlayerScore2 >= 100:
    print("Player 2 Wins!")
else:
    print("Error.")

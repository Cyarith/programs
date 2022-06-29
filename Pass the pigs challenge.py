#Objective 8: Challenges
#Pass the pigs challenge
def Roll():
    import random
    b = random.randint(1,5)
    return b
#Main program
PlayerScore = 0
PigA = 0
PigB = 0 
while PlayerScore < 100:
    input("")
    print("")
    PigA = Roll()
    PigB = Roll()
    if PigA == PigB and PigA == 2:
        print("Sider + 1 point")
        PlayerScore = PlayerScore + 1
    elif PigA == PigB and PigA == 3:
        print("Sider + 1 point")
        PlayerScore = PlayerScore + 1
    elif PigA == 1 or PigB == 1:
        print("Trotter + 5 points")
        PlayerScore = PlayerScore + 5
    elif PigA == PigB and PigA == 1:
        print("Double Trotter + 20 points")
        PlayerScore = PlayerScore + 20
    elif PigA == 4 or PigB == 4:
        print("Snouter + 5 points")
        PlayerScore = PlayerScore + 5
    elif PigA == PigB and PigA == 4:
        print("Double Snouter + 20 points")
        PlayerScore = PlayerScore + 20
    elif PigA == 5 or PigB == 5:
        print("Razorback + 5 points")
        PlayerScore = PlayerScore + 5
    elif PigA == PigB and PigA == 5:
        print("Double Razorback + 20 points")
        PlayerScore = PlayerScore + 20
    else:
        print("Pig Out - Reset to 0")
        PlayerScore = 0
    print("Your Score is",PlayerScore)
        

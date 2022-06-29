#Objective 8: Challenges
#Darts Challenge
PlayerScore = 501
while PlayerScore != 0:
    DartTotal = int(input("Enter the total of your 3 darts: "))
    PointReduction = PlayerScore - DartTotal
    if PointReduction >= 1:
        PlayerScore = PlayerScore - DartTotal
        print("Your new score is",PlayerScore)
    elif PointReduction == 0:
        PlayerScore = PlayerScore - DartTotal
        print("Player 1 wins")
        PlayerScore = 501
    else:
        print("L")

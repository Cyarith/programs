#Objective 7: Challenge
#XP Challenge
TotalXP = 0
PlayerRank = 1
GameXP = 0
while TotalXP < 2000:
    GameXP = int(input("Enter how much exp you gained in the last game: "))
    TotalXP = TotalXP + GameXP
    if TotalXP >= 100 and PlayerRank == 1:
        TotalXP = TotalXP - 100
        PlayerRank = PlayerRank + 1
        print("You have been promoted!")
        print("You are now a rank",PlayerRank,"Corporal")
    elif TotalXP >= 300 and PlayerRank == 2:
        TotalXP = TotalXP - 300
        PlayerRank = PlayerRank + 1
        print("You have been promoted!")
        print("You are now a rank",PlayerRank,"Sergeant")
    elif TotalXP >= 700 and PlayerRank == 3:
        TotalXP = TotalXP - 700
        PlayerRank = PlayerRank + 1
        print("You have been promoted!")
        print("You are now a rank",PlayerRank,"Staff Sergeant")
    elif TotalXP >= 1500 and PlayerRank == 4:
        PlayerRank = PlayerRank + 1
        print("You have been promoted!")
        print("You are now a rank",PlayerRank,"Warrant Officer")
    else:
        TotalXP = TotalXP
    if PlayerRank == 1:
        print("You're at",TotalXP,"/100 XP")
    elif PlayerRank == 2:
        print("You're at",TotalXP,"/300 XP")
    elif PlayerRank == 3:
        print("You're at",TotalXP,"/700 XP")
    elif PlayerRank == 4:
        print("You're at",TotalXP,"/1500 XP")
    else:
        print("You're at",TotalXP," XP")
        print("You have exceeded maximum rank.")

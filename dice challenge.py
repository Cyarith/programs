#2 player dice game challenge
def Roll():
    import random
    a = random.randint(1,6)
    b = random.randint(1,6)
    if (a+b)/2 == (a+b)//2:
        c = a+b + 10
    else:
        c = a+b-5
    if a == b:
        d = random.randint(1,6)
        c = a+b+d
    return c
#main
run = True
choice = 0
passwordfile1 = open("password.txt","r") #opens the file for registered users
passwordfile2 = open("password.txt","r") #for player 2 login
registerfile = open("password.txt","a") # opens file in append mode, for new users
winfile = open("dicegamewins.txt","a") #opens winner's file in append mode
winprint = open("dicegamewins.txt","r") #opens winner's file in read mode
registeredpass1 = 0
registeredname1 = 0
loggedin1 = False
loggedin2 = False
registeredpass2 = 0
registeredname2 = 0
newname = 0
newpass = 0
userpass = 1
user2name = ""
user1name = ""
user1score = 0
user2score = 0
Round = 0
end = False
RollOne = 0
RollTwo = 0
while end == False:
    if userpass == 1:
        run = True
        print("Player 1")
        print("1. Login")
        print("2. New Player")
        print("3. Play")
        choice = input("")
        if choice == "1":
            registeredname1 = input("Enter your username: ")
            registeredpass1= input("Enter your password: ")
            for i in range(50):
                print(" ")
            while run == True:
                passline = passwordfile1.readline()
                passes = passline.split(", ")
                filepass = passes[1].split("\n")
                if registeredname1 == passes[0] and registeredpass1 == filepass[0]:
                    print("======================")
                    print("Sucessfully logged in.")
                    print("======================")
                    user1name = registeredname1
                    loggedin1 = True
                    run = False
                    userpass = 2
                else:
                    print("Your username or password did not match this user.")
                if passline == "":
                    run = False
        elif choice == "2":
            print("Registering you as a new user.")
            newname = input("Enter your username: ")
            newpass = input("Enter your password: ")
            registerfile.write("\n"+newname+", "+newpass)
            print("========================================")
            print("Sucessfully registered you as a new user")
            print("========================================")
            user1name = newname
            registerfile.close()
            registerfile = open("password.txt","a")
            userpass = 2
            loggedin1 = True
        elif choice == "3":
            print("Log in first!")
    elif userpass == 2:
        run = True
        print("Player 2")
        print("1. Login")
        print("2. New Player")
        print("3. Play")
        choice = input("")
        if choice == "1":
            registeredname2 = input("Enter your username: ")
            registeredpass2 = input("Enter your password: ")
            for i in range(50):
                print(" ")
            while run == True:
                passline = passwordfile2.readline()
                passes = passline.split(", ")
                filepass = passes[1].split("\n")
                if registeredname2 == passes[0] and registeredpass2 == filepass[0]:
                    print("======================")
                    print("Sucessfully logged in.")
                    print("======================")
                    user2name = registeredname2
                    loggedin2 = True
                    run = False
                    userpass = 3
                else:
                    print("Your username or password did not match this user.")
                if passline == "":
                    run = False
        elif choice == "2":
            print("Registering you as a new user.")
            newname = input("Enter your username: ")
            newpass = input("Enter your password: ")
            registerfile.write("\n"+newname+", "+newpass)
            print("========================================")
            print("Sucessfully registered you as a new user")
            print("========================================")
            user2name = newname
            registerfile.close()
            registerfile = open("password.txt","a")
            userpass = 3
            loggedin2 = True
        elif choice == "3":
            print("User 2 is not logged in")
    elif userpass == 3:
        print(user1name,"Logged in as Player 1")
        print(user2name,"Logged in as Player 2")
        print("Press Enter to play")
        choice = input("")
        while Round < 5:
            Round += 1
            print("Round",Round)
            print("Player 1's Turn")
            print("Press enter to roll")
            input("")
            RollOne = Roll()
            user1score += RollOne
            print(user1name,"Gained",RollOne)
            print("Your total score is now",user1score)
            print("")
            print("============ Next Player ===========")
            print("")
            print("Round",Round)
            print("Player 2's Turn")
            print("Press enter to roll")
            input("")
            RollTwo = Roll()
            user2score += RollTwo
            print(user2name,"Gained",RollTwo)
            print("Your total score is now",user2score)
            print("====================================")
            print("============ Next Round ============")
            print("====================================")
        if user1score > user2score:
            winscore = str(user1score)
            print(user1name,"Wins!")
            print(user1name,user1score)
            print(user2name,user2score)
            print("Adding you to the winner's file")
            winfile.write("\n"+user1name+", "+winscore)
            winfile.close()
            end = True
        elif user2score > user1score:
            winscore = str(user2score)
            print(user2name,"Wins!")
            print(user2name,user2score)
            print(user1name,user1score)
            print("Adding you to the winner's file")
            winfile.write("\n"+user2name+", "+winscore)
            winfile.close()
            end = True
        else:
            while user2score == user1score:
                print("Scores Tied")
                print(" - TIEBREAKER ROUND - ")
                RollOne = Roll()
                RollTwo = Roll()
                user1score += RollOne
                user2score += RollTwo
                if user1score > user2score:
                    winscore = str(user1score)
                    print(user1name,"Wins!")
                    print(user1name,user1score)
                    print(user2name,user2score)
                    print("Adding you to the winner's file")
                    winfile.write("\n"+user1name+", "+winscore)
                    winfile.close()
                    end = True
                elif user2score > user1score:
                    winscore = str(user2score)
                    print(user2name,"Wins!")
                    print(user2name,user2score)
                    print(user1name,user1score)
                    print("Adding you to the winner's file")
                    winfile.write("\n"+user2name+", "+winscore)
                    winfile.close()
                    end = True
                else:
                    print("Tied, Rerunning tiebreaker")
        

    else:
        print("userpass Error")
    
winline = winprint.readline()


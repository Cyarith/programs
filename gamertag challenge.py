#Objective 7: Challenges
#Gamertag challenge
#The program will check the length of the gamerTags entered
valid_gamertag = True
gamerTag = input("Enter a gamertag less than 15 characters:")
gamertag_length = len(gamerTag)
if gamertag_length > 15:
    print("Your gamertag is too long.")
    print("Gamertags must be less than 15 characters.")
else:
    print("Gamertag",gamerTag,"accepted.")

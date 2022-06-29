#Global variables accessed by all subroutines
MaxNoOfStars=0
NoOfStars=0
NoOfSpaces=0
#Set the size of the pyramid of stars
def InitialiseNoOfSpacesAndStars():
    global NoOfSpaces, MaxNoOfStars, NoOfStars
    MaxNoOfStars=int(input("How many stars at the base (1-40)? "))
    #Calculate spaces needed from tip
    NoOfSpaces = MaxNoOfStars // 2
    #Set tip of pyramid to one star
    NoOfStars = 1
#Outputs spaces before stars
def OutputLeadingSpaces():
    global NoOfSpaces
    for count in range(NoOfSpaces):
        print("-",end="")
#Outputs stars
def OutputLineOfStars():
    global NoOfStars
    for count in range(NoOfStars):
        print("_",end="")
    #Move to next line
    print()
#Adjusts number of stars & spaces after output
def AdjustNoOfSpacesAndStars():
    global NoOfSpaces, NoOfStars
    NoOfSpaces = NoOfSpaces - 1
    NoOfStars = NoOfStars + 2
#Main program starts here
InitialiseNoOfSpacesAndStars()
while NoOfStars <= MaxNoOfStars:
    OutputLeadingSpaces()
    OutputLineOfStars()
    AdjustNoOfSpacesAndStars()

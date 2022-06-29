#Objective 9: Challenges
#Notebook Challenge
Line1 = ""
Line2 = ""
Line3 = ""
Line4 = ""
Line5 = ""
Line6 = ""
Line7 = ""
Line8 = ""
Line9 = ""
Line10 = ""
LineSelect = 1
run = True
while run == True:
    print("1",Line1)
    print("2",Line2)
    print("3",Line3)
    print("4",Line4)
    print("5",Line5)
    print("6",Line6)
    print("7",Line7)
    print("8",Line8)
    print("9",Line9)
    print("10",Line10)
    LineSelect = int(input("Enter the number of the line you would like to edit: "))
    if LineSelect == 1:
        Line1 = input("Enter the note you would like to add: ")
    elif LineSelect == 2:
        Line2 = input("Enter the note you would like to add: ")
    elif LineSelect == 3:
        Line3 = input("Enter the note you would like to add: ")
    elif LineSelect == 4:
        Line4 = input("Enter the note you would like to add: ")
    elif LineSelect == 5:
        Line5 = input("Enter the note you would like to add: ")
    elif LineSelect == 6:
        Line6 = input("Enter the note you would like to add: ")
    elif LineSelect == 7:
        Line7 = input("Enter the note you would like to add: ")
    elif LineSelect == 8:
        Line8 = input("Enter the note you would like to add: ")
    elif LineSelect == 9:
        Line9 = input("Enter the note you would like to add: ")
    elif LineSelect == 10:
        Line10 = input("Enter the note you would like to add: ")
    else:
        print("Error")
    

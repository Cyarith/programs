#Objective 9: Challenges
#Battleships Challenge
column = [0]*10
direction = 0
i = 1
b = 1
c = 1
shiptype = 0
rows = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]
shipcolumn = int(input("Enter a number 0-9, which column you would like to put your ship on"))
shiprow = int(input("Enter a number 0-9, which row you would like to put your ship on"))
rows[shiprow][shipcolumn] = 1
shiptype = int(input("Enter the shipe size you want to place"))
direction = input("Would you like to place the ship horizontally or vertically?")

if direction == "Vertical" or direction == "vertical" or direction == "Vertically" or direction == "vertically":
    while shiprow+shiptype-i > shiprow:
        if shiprow+shiptype > 9:
            rows[shiprow][shipcolumn] = 0
            shiprow = int(input("The ship will go off the board. Please select
        else:
            rows[shiprow+shiptype-i][shipcolumn] = 1
            i = i + 1 
elif direction == "Horizontal" or direction == "horizontal" or direction == "horizontally" or direction == "Horizontally":
    while shipcolumn+shiptype-b > shipcolumn:
        if shipcolumn+shiptype > 9:
            rows[shiprow][shipcolumn] = 0
            shipcolumn = int(input("The ship will go off the board. Please select another column: "))
            rows[shiprow][shipcolumn] = 1
        else:
            rows[shiprow][shipcolumn+shiptype-b] = 1
            b = b + 1
else:
    print("Error")
i = 0
b = 0
print(rows)
print("You have placed a ship on square",shiprow,shipcolumn)

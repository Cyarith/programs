maximum = int(input("Enter the maximum number that can be guessed "))
minimum = 1
Searches = 0
TargetNumber = int(input("What is the number? "))
Midpoint = (maximum+minimum) // 2
while TargetNumber != Midpoint:
    if TargetNumber < Midpoint:
        maximum = Midpoint-1
        Searches = Searches + 1
    else:
        minimum = Midpoint+1
        Searches = Searches + 1
    Midpoint = (maximum+minimum)//2
print("Your number has been found!")
print("It took",Searches,"Attempts to find your number")




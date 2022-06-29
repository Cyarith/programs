count = 0
runningTotal = 0 
number = int(input("Please input a number"))
while number >= 0:
    count = count+1
    runningTotal = runningTotal + number
    nextnumber = int(input("Please enter a second number"))
print("You entered",count,"numbers")
print("Total =",runningTotal)

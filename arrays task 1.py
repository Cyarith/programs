averagerain = 0
totalrain = 0
aboveaverage = 0
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rainfall = [0]*12
for i in range(0, 12):
    print("Enter the rainfall for", month[i])
    rainfall[i] = float(input())
for i in range(0,12):
    print(month[i],"       ",rainfall[i])
    averagerain += rainfall[i]
    totalrain += rainfall[i]
averagerain = averagerain / 12
for i in range(0,12):
    if rainfall[i] > averagerain:
        aboveaverage += 1
    else:
        aboveaverage = aboveaverage
print("The total rainfall was",totalrain)
print("The average annual rainfall was",averagerain)
print(aboveaverage,"Months had above average monthly rainfall")

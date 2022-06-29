#objective 6: challenges
#average calculator challenge
#program that allows the user to enter how many numbers to be averaged, the user then enters them and the program calculates the mean
numberamount = int(input("how many numbers do you have? "))
total = 0
for counter in range(numberamount):
    counter = int(input("enter a number"))
    total = total + counter
average = float(total/numberamount)
print("your average is",average)

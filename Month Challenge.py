#Objective 5: Challenge
#Month challenge
#program that allows the user to enter a number between 1 and 12 and displays the month name and amount of days in it
MonthNumber = int(input("Enter a number 1 to 12 to find a month "))
CurrentYear = int(input("Enter the current year "))
Remainder = CurrentYear % 4
if Remainder == 0:
    print("It is a leap year!")
    if MonthNumber == 1:
        print("January, 31 Days")
    elif MonthNumber == 2:
        print("February, 29 Days")
    elif MonthNumber == 3:
        print("March, 31 Days")
    elif MonthNumber == 4:
        print("April, 30 Days")
    elif MonthNumber == 5:
        print("May, 31 Days")
    elif MonthNumber == 6:
        print("June, 30 Days")
    elif MonthNumber == 7:
        print("July, 31 Days")
    elif MonthNumber == 8:
        print("August, 31 Days")
    elif MonthNumber == 9:
        print("September, 30 Days")
    elif MonthNumber == 10:
        print("October, 31 Days")         
    elif MonthNumber == 11:
        print("November, 30 Days")
    elif MonthNumber == 12:
        print("December, 31 Days")
else:
    print("It is not a leap year")
    if MonthNumber == 1:
        print("January, 31 Days")
    elif MonthNumber == 2:
        print("February, 28 Days")
    elif MonthNumber == 3:
        print("March, 31 Days")
    elif MonthNumber == 4:
        print("April, 30 Days")
    elif MonthNumber == 5:
        print("May, 31 Days")
    elif MonthNumber == 6:
        print("June, 30 Days")
    elif MonthNumber == 7:
        print("July, 31 Days")
    elif MonthNumber == 8:
        print("August, 31 Days")
    elif MonthNumber == 9:
        print("September, 30 Days")
    elif MonthNumber == 10:
        print("October, 31 Days")         
    elif MonthNumber == 11:
        print("November, 30 Days")
    elif MonthNumber == 12:
        print("December, 31 Days")

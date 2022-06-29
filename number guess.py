print("Think of a number from 1 to 1000!") 
maximum = 1000
minimum = 1
searches = 1
midpoint = (maximum+minimum)//2
print("Enter Lower if your number is below the guess.")
print("Enter Higher if your number is above the guess.")
print("Enter True if your number is the guess")
print("MAKE SURE TO USE A CAPITAL LETTER AT THE START")
number = input("is your number 500? ")
while number != "True":
    if number == "Lower":
        maximum = midpoint-1
        searches = searches+1
    elif number == "lower":
        maximum = midpoint-1
        searches = searches +1
    elif number == "Higher":
        minimum = midpoint+1
        searches = searches+1
    elif number == "higher":
        minimum = midpoint+1
        searches = searches+1
    else:
        print("Please enter Higher, Lower or True to the previous question.")
        print("Make sure you use caps when responding.")
    midpoint = (maximum+minimum)//2
    print(midpoint)
    number = input("is that your number?")
print("It took",searches,"Attempts to find your number")

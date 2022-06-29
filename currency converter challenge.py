#Objective 9: Challenges
#Currency converter challenge
currencies = ["Euro", "USD", "Bitcoin", "Vietnamese dong", "Yen"]
rate = [1.15, 1.39, 0.000025, 31967.27, 151.53]
conversion = 0
choice = 0
amount = 0
run = True
while run == True:
    for r in range(5):
        print("Would you like to convert Pound Sterling to",currencies[r])
        choice = input("")
        if choice == "yes" or choice == "Yes":
            amount = int(input("Enter the amount of Pound Sterling to convert: "))
            conversion = amount * rate[r]
            print(amount," Pound Sterling is equal to",conversion,"",currencies[r],)
            print("The conversion rate from Pound Sterling to",currencies[r],"is",rate[r])
            print("")
        elif choice == "no" or choice == "No":
            conversion = conversion
        else:
            print("Could not understand your response")
            
            
            

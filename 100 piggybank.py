#program that will allow the user to add money into a piggybank until £100
Piggybank =  0
while Piggybank < 100:
    MoneyAdded = float(input("How much money would you like to add in the piggybank? "))
    Piggybank = Piggybank + MoneyAdded
    MoneyNeeded = 100 - Piggybank
    print("You need to save £",MoneyNeeded,"More to get to £100!")
    

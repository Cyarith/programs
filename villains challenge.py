#Super villains worksheet challenge
totalWage = 0
villains = ["The Joker","Magneto","Red Mist","Doc Ock"]
for counter in range(4):
    print(villains[counter])
villainWages = [21,17,3,5]
for counter in range(4):
    print(villains[counter],": £",villainWages[counter],"million")
    totalWage = totalWage + villainWages[counter]
print("The total bill is £",totalWage,"million")    

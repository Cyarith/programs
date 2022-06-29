#Objective 4: Challenges
#Water temperature challenge
#program that reads the temperature of water in a container in centigrade and says if the water if frozen, boiling or neither
WaterTemp = int(input("Enter the temperature of the water "))
if WaterTemp > 100:
    print("Boiling Water")
elif WaterTemp < 0:
    print("Freezing Water")
else:
    print("Normal Temperature Water")                

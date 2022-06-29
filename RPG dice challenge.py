#Objective 5: Challenges
#RPG dice challenge
#program that asks the user how many sides a dice has and outputs a random number for the dice
import random
DiceRange = int(input("Enter the maximum number the dice can roll "))
RandomNumber = random.randint(1,DiceRange)
print("Your Random Number is",RandomNumber)

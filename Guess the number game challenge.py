#Objective 7: Challenges
#Guess the number game challenge
import random
CorrectNumber = random.randint(1,100)
PlayerGuess = int(input("Guess a number 1 to 100:"))
GuessAmount = 1
while PlayerGuess != CorrectNumber:
    if PlayerGuess > CorrectNumber:
        print("too high!")
        PlayerGuess = int(input("Guess a number between 1 and 100:"))
    elif PlayerGuess < CorrectNumber:
        print("too low!")
        PlayerGuess = int(input("Guess a number between 1 and 100:"))
    else:
        print("Correct, the number was",CorrectNumber)
    GuessAmount = GuessAmount + 1
print("You used",GuessAmount,"Guesses")

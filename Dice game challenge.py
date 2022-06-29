#Objective 5:Challenges
#Dice game challenge
#program that will calculate the score in a dice game
import random
number1 = random.randint(1,6)
number2 = random.randint(1,6)
number3 = random.randint(1,6)
if number1 == number2 == number3:
    Score = number1+number2+number3
    print("All 3 dice rolled the same and got",Score)
elif number1 == number2:
    Score = number1+number2
    Score = Score - number3
    print("2 of the dice rolled the same and got",Score)
elif number1 == number3:
    Score = number1+number3
    Score = Score - number2
    print("2 of the dice rolled the same and got",Score)
elif number2 == number3:
    Score = number2+number3
    Score = Score - number1
    print("2 of the dice rolled the same and got",Score)
else:
    Score = 0
    print("none of the dice rolled the same so you ended up with",Score)
    

#rolling 2 dice game
score = 0
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
if dice1 != dice2:
    score = dice1+dice2
    print("Your rolled",dice1,"and",dice2,"your score is",score)
else:
    if dice1 == 6:
        score = 0
        print("You rolled a double 6... your score is",score)
    else:
        score = (dice1+dice2)*2
        print("You rolled a double",dice1,"your score is",score)
        

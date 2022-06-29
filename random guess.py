import random
number = random.randint(1,100)
attempts = 1
guess = int(input("Guess a number from 1 to 100 "))
while guess != number:
    guess = int(input("Incorrect, try another number "))
    if guess == number:
        print("Correct!you took",attempts,"attempts")
    elif guess < number:
        print("Too low!")
        attempts = attempts+1
    else:                 
        print("Too high!")
        attempts = attempts+1
            
    

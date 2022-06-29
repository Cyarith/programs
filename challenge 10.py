#Challenge 10
def roll():
    import random
    a = ["Rock","Paper","Scissors"]
    b = random.choice(a)
    return b
#Main
choice = input("Enter Rock, Paper or Scissors: ")
computerchoice = roll()
if choice == "Rock" and computerchoice == "Rock" or choice == "Paper" and computerchoice == "Paper" or choice == "Scissors" and computerchoice == "Scissors":
    print("Draw")
    print("You drew",choice)
    print("Computer drew",computerchoice)
elif choice == "Rock" and computerchoice == "Paper" or choice == "Paper" and computerchoice == "Scissors" or choice == "Scissors" and computerchoice == "Rock":
    print("You lost")
    print("You drew",choice)
    print("Computer drew",computerchoice)
elif choice == "Rock" and computerchoice == "Scissors" or choice == "Paper" and computerchoice == "Rock" or choice == "Scissors" and computerchoice == "Paper":
    print("You won")
    print("You drew",choice)
    print("Computer drew",computerchoice)
else:
    print("Could not recognise your response")

#Objective 7: Challenges
#Compound interest challenge
#program that shows how compound interest grows in a bank savings account.
CurrentBalance = float(input("Enter your current balance:"))
InterestRate = float(input("Enter your interest rate, 0.01 being 1%:"))
DesiredBalance = float(input("Enter the balance you would like to reach:"))
InterestMultiplier = float(InterestRate + 1)
Years = int(0)
while CurrentBalance < DesiredBalance:
    CurrentBalance = CurrentBalance * InterestMultiplier
    Years = Years + 1
    print("After",Years,"years, your balance is now",CurrentBalance)
         

#Objective 6: challenges
#times table challenge 1
#program that allows the user to enter a number between 1 and 12 and then outputs the times table for the number
originalnumber = int(input("enter a number between 1 and 12 "))
number = originalnumber 
amount = int(input("how many times iterations do you want? "))
for i in range(amount):
    print(number)
    number = number + originalnumber
    

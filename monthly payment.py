#program that will allow the user to add payments for 12 months
money = 0
for month in range(1,13):
    payment = float(input("How much money will you add this month?" ))
    money = money+payment
print("You have paid £",money,"over the course of 12 months")                  
    

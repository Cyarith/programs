#code that runs a for loop for pocket money starting at 1p, doubling every week
pocketMoney = 0.01
totalMoney = 0.01
for week in range(1,26):
    print("The Current week is",week)
    print("You will get £",pocketMoney)
    pocketMoney = pocketMoney*2
    totalMoney = totalMoney + pocketMoney
print("Congrats! you have earned",totalMoney)    
input("press ENTER to exit")    

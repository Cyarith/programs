#Objective 8: Challenges
#VAT Challenge
def VAT(a):
    b = a*0.2
    return b
def NewPrice(a):
    c = a*1.2
    return c
#main program
ItemPrice = float(input("Enter the price of the item: "))
print("The new price for the item after VAT is",NewPrice(ItemPrice))
print("You will be paying",VAT(ItemPrice),"In VAT")

#Objective 8: Challenges
#VAT CHALLENGE
#Program that asks the user for the price of an item and then returns the VAT for it
def VAT(a):
 addedprice = a * 0.2
 if addedprice > 0:
     return addedprice
 else:
     return 0

#main program
itemprice = int(input("What is the price of the item? "))
print("The VAT is",VAT(itemprice))

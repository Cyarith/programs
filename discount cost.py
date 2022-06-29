Price = float(input("What is the price of your items?"))
if Price >=50:
    print("Applicable for discount")
    Discount = Price /10
    DPrice = Price - Discount
    print("Discount applied, Total:",DPrice)
else:
    print("Price Charged. Inapplicable for discount.")

            
        

Name = input("Please Enter Your Name.")
PhoneMinutes = int(input(Name+"How many minutes of calling have you used this month?"))
CallPrice = PhoneMinutes * 0.10
PhoneText = int(input(Name+"How many texts have you sent this month?"))
TextPrice = PhoneText * 0.05
TotalBill = TextPrice + CallPrice
print("Your total bill is",TotalBill)                
VATAddition = TotalBill / 5
VATTotal = VATAddition + TotalBill
print("Your total bill including VAT is",VATTotal)                
                
                

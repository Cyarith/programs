#Times table, percentage and VAT calculator program
#Vat calculator
def Vat(a):
    b = a*1.2
    return b
#Times table calculator
def TimesTable(a,b):
    c = a*b
    return c
#Percentage calculator
def PercentCalculator(a,b):
    c = (a/100)*b
    return c
#Main program
Menu_Selection = 1
Number = 0
Number2 = 0
print("Welcome to the life calculator")
print("Select a number 1 to 3")
print("1. Vat calculator")
print("2. Times table calculator")
print("3. Percentage calculator")
while Menu_Selection == Menu_Selection:
    Menu_Selection = int(input("Enter your number selection here: "))
    if Menu_Selection == 1:
        Number = float(input("Enter a number to add VAT to: "))
        print("Your Original Number was",Number)
        print("With Vat, your number is",Vat(Number))
    elif Menu_Selection == 2:
        Number = int(input("Enter your first number to mulitply: "))
        Number2 = int(input("Enter your second number to multiply: "))
        print("Your numbers were",Number,"and",Number2)
        print("Multiplied together, your final number is",TimesTable(Number,Number2))
    elif Menu_Selection == 3:
        Number = int(input("Enter your base number: "))
        Number2 = int(input("Enter the percentage you want of your base number: "))
        print("You chose",Number2,"% of",Number)
        print("Your final number is",PercentCalculator(Number,Number2))
    else:
        print("Number Invalid, Please Re-Enter")
    print("")
    print("Welcome to the life calculator")
    print("Select a number 1 to 3")
    print("1. Vat calculator")
    print("2. Times table calculator")
    print("3. Percentage calculator")
        

#Objective 7: Challenges
#Happy numbers challenge
numbercheck = int(input("enter a number "))
numberslot = str(numbercheck)
counter = 0
digitsum = 0
numbertotal = 0
while 1==1:
    numberslot = str(numbercheck)
    slotnumber = numberslot[counter]
    print(slotnumber)
    slotint = int(slotnumber)
    print(slotint)
    calculation = slotint*slotint
    print(calculation)
    numbertotal = numbertotal + calculation
    numberlength = len(numberslot)
    if counter < numberlength:
        counter = counter + 1
    else:
        counter = 0
        numbercheck = numbertotal

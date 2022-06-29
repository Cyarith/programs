#Objective 5: Challenges
#Divisible challenge
#program that asks the user for 2 numbers, then outputs if the numbers are exactly divisible by eachother, if not, it outputs the remainder
NumberA = int(input("Enter a number that will divide into another"))
NumberB = int(input("Enter a number that will be divided by the previous number"))
Remainder=NumberB % NumberA
DivisionAmount = NumberB / NumberA
if Remainder == 0:
    print(NumberB,"can be divided by",NumberA)
elif Remainder == NumberB:
    print(NumberA,"was larger than",NumberB)
elif NumberA == 0:
    print("Error:0 cannot divide into any number")
else:    
    print(NumberB,"cannot be divided by",NumberA,"there was a remainder of",Remainder)
    
    

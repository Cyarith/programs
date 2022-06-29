#Objective 4: Challenges
#Greatest number challenge
#program that displays the larger of 2 numbers entered
NumberA = int(input("Enter a number "))
NumberB = int(input("Enter a second number "))
if NumberA > NumberB:
    print(NumberA,"is larger than",NumberB)
elif NumberB > NumberA:
    print(NumberB,"is larger than",NumberA)
elif NumberA == NumberB:
    print(NumberA,"and",NumberB,"are equal")
else:
    print("Could not read the numbers, Please make sure there are no letters or punctuation")
    

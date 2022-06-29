#Objective 4: Challenges
#Vocational grade challenge
#Program that allows the user to enter a mark out of 100 and prints FAIL for scores below 40,PASS for a score above 40,MERIT for a score above 60 and DISTINCTION for a score above 80
Grade = int(input("Enter the student's grade out of 100 "))
if Grade < 40:
    print("FAIL")
elif Grade > 80:
    print("DISTINCTION")
elif Grade > 60:
    print("MERIT")
elif Grade > 40:
    print("PASS")

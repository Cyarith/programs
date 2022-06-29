#program that can input student's score & outputs a percentage and level
#teacher inputs marks available & student's name and score
StudentName = input("Input the Student's name: ")
StudentScore = int(input("Input the Student's score: "))
MaxMarks = int(input("Input the maximum amount of marks on the paper: "))
StudentPercentage = StudentScore // (MaxMarks / 100)
if StudentPercentage >= 87:
    print(StudentName,"Has got",StudentPercentage,"% and level 9")
elif StudentPercentage >= 80:
    print(StudentName,"Has got",StudentPercentage,"% and level 8")
elif StudentPercentage >= 75:
    print(StudentName,"Has got",StudentPercentage,"% and level 7")
elif StudentPercentage >= 70:
    print(StudentName,"Has got",StudentPercentage,"% and level 6")
elif StudentPercentage >= 62:
    print(StudentName,"Has got",StudentPercentage,"% and level 5")
elif StudentPercentage >= 54:
    print(StudentName,"Has got",StudentPercentage,"% and level 4")
elif StudentPercentage >= 32:
    print(StudentName,"Has got",StudentPercentage,"% and level 3")
elif StudentPercentage >= 26:
    print(StudentName,"Has got",StudentPercentage,"% and level 2")
elif StudentPercentage >= 18:
    print(StudentName,"Has got",StudentPercentage,"% and level 1")
else:
    print(StudentName,"Has got",StudentPercentage,"% and is UNGRADEABLE")


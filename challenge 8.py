#Challenge 8
mark = int(input("How many marks did you get?: "))
grade = 0
if mark >= 75:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 35:
    grade = "C"
else:
    grade = "D"
print("you got a grade",grade)

marksFile = open("marks.txt","r")
print("Checking for the highest mark")
moreLines = True
Lastmark = 0
topstudents = []
while moreLines:
    markRec = marksFile.readline()
    if markRec == "":
        moreLines = False
    else:
        field = markRec.split(",")
        name = field[0]
        mark = int(field[1])
        if mark > Lastmark:
            topstudents = []
            Lastmark = mark
            bestname = name
        elif mark == Lastmark:
            topstudents.append(name)
print(bestname,"had the highest marks with",Lastmark,"marks!")
print("The following students also gained",Lastmark,"marks")
print(topstudents)
marksFile.close()
        

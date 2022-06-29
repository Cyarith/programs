marksFile = open("marks.txt","a") #a opens the file in append mode
moreNames = True

while moreNames:
    name = input("Enter a student's name: ")
    mark = input("Enter the student's mark: ")
    marksFile.write("\n" + name + ", " + mark)
    if input("Add another student (y/n)? ") == "n":
        moreNames = False

marksFile.close()


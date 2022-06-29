marksFile = open("marks.txt","r") #r opens the file in reading mode
print("the marks file has been opened in reading mode")
endOfLine = True
while endOfLine == True:
    line = marksFile.readline()
    print(line)
    if line == "":
        endOfLine = False
marksFile.close()

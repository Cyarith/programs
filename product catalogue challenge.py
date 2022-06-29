#Objective 10: Challenges
#Product catalogue challenge
new = True
catalogue = open("catalogue.txt","a")
read = open("catalogue.txt","r")
endOfLine = True
while endOfLine == True:
    line = read.readline()
    print(line)
    if line == "":
        endOfLine = False
while new == True:
    code = input("Enter the code for the product: ")
    description = input("Enter the description for the product: ")
    price = input("Enter the price for the product: ")
    catalogue.write(code+", "+description+", "+price)
    newitem = input("Would you like to add another item?: ")
    if newitem == "Yes" or newitem == "yes":
        new = True
    else:
        new = False
        print("End")
catalogue.close()
marksFile.close()

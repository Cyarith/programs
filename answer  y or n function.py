def answerYorN():
    answer = 0
    while answer != "y" or answer != "Y" or answer != "n" or answer != "N": 
        answer = input("Y or N?: ")
        if answer == "y" or answer == "Y":
            return "y"
        elif answer == "n" or answer == "N":
            return "n"
        else:
            print("Invalid response")
#main program
response = answerYorN()
print(response)

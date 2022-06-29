#Objective 3: Challenges
#Name seperator challenge
#program that allows the user to enter their full name on one line then separate them and print it.
Fullname = input("Enter your full name(firstname and secondname)")
WhiteSpace = Fullname.find(" ")
Forename = Fullname[:WhiteSpace]
Surname = Fullname[-WhiteSpace:]
print("Firstname:",Forename)
print("Surname:",Surname)


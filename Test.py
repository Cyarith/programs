print("hello! What is your first name?") #Asks the user what their firstname is
firstName = input()
print("Hi ",firstName," What is your surname?") #Asks the user what their surname is
surname = input()
print("Hello ,",firstName,surname) #Says hello to the user addressing their full name
fullName = firstName + " " + surname
print(fullName) #Says the user's full name
print(surname.upper(),firstName) #Says the user's surname is capitals then first name in lowercase
surnameLetters = len(surname)
firstNameLetters = len(firstName)
print("Your surname has",surnameLetters,"letters")
print("Your username is",surname[0]+""+surname[1]+""+surname[2]+""+firstName[0]+""+str(surnameLetters)) #Creates a username for the user using the first 3 letters of the surname, first initial of the firstname and the amount of letters in the surname
print("Your other username could be",firstName[0]+""+firstName[1]+""+firstName[2]+""+str(surnameLetters)+""+str(firstNameLetters)) #Creates a second username using another combination of firstName letters and number of letters in the firstName and Surname
print("Now is time to ask you some questions,",fullName)
print("1.Which Country do you live in?")#Asks the user what country they live in
homeCountry = input()#Stores what the user says the country they are living in is
print("i grew up in",homeCountry)
print("2.What if your favourite food?")#Asks the user what their favourite food is
favouriteFood = input() #Stores what the user says their favourite food is
print("I used to eat",favouriteFood,"in my childhood too!")
print("3.What is your favourite school subject?")#Asks thr user what their favourite school subject is
schoolSubject = input() #Stores what the user says their favourite school subject is
print("I, myself studied",schoolSubject," in school")

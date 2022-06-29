#validation password system
LongPass = "False"
while LongPass == "False":
    password = input("enter a password longer than 8 characters ")
    if len(password) >= 8:
        LongPass = "True"
    else:
        print("Your password is too short")

EnterPass = input("Enter your password - CASE SENSITIVE: ")
if EnterPass == password:
    print("Password correct!")
else:
    print("Incorrect password")

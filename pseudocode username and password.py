#username and password pseudocode
UserPassword = "a"
counter = 0
password = "APC254"
for i in range(3):
    if UserPassword != password:
        UserPassword = input("Enter password:")
    else:
        password = password
if UserPassword == password:
    print("Password Correct")
else:
    print("Access denied")

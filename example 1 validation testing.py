isLongEnough = False

while not isLongEnough:
    password = input('Enter password at least 5 characters: ')
    if len(password) >= 5:
        isLongEnough = True
    else:
        print('Password entered is too short')

print('Your password entered is: ' + password)

#Reference: http://easypythondocs.com/validation.html#definition

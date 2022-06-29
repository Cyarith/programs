#Objective 6: challenges
#fibonacci sequence challenge
firstnumber = 0
secondnumber = 1
for i in range(20):
    nextnumber = firstnumber + secondnumber
    print(nextnumber)
    firstnumber = secondnumber
    secondnumber = nextnumber

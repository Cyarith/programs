#Objective 6: challenges
#9 green bottles challenge
#program that allows the user to enter an amount of green bottles
bottles = int(input("How many green bottles are there? "))
for i in range(bottles):
    if bottles == 1:
        print("there is",bottles,"green bottle sitting on the wall")
    else:
        print("there are",bottles,"green bottles sitting on the wall")
    bottles = bottles-1


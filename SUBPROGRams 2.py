#Program to output a set of random numbers
import random
#Output random numbers
def outputrandoms(n,m):
    for counter in range(1,n+1):
        randomnum = random.randint(1,m)
        print("Number",counter,"is",randomnum)
#Main program starts here
number=int(input("How many numbers do you want to output? "))
maximum=int(input("What is the maximum number? "))
outputrandoms(number, maximum)

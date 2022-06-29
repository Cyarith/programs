def addIntegers(a,b):
    counter = 0
    c = 0
    while b-counter >= a:
        c += b-counter
        counter += 1
    return c
#main
lowerbound = int(input("Enter a lower bound to add: "))
upperbound = int(input("Enter an upper bound to add: "))
print("Adding numbers between",lowerbound,"and",upperbound)
print(addIntegers(lowerbound,upperbound))

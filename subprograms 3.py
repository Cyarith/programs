#How functions can be used
#Returns a positive number from subtraction
def floor(a, b):
    f = a - b
    if f > 0:
        return f
    else:
        return 0
#Main program starts here
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The floor number is:",floor(num1, num2))

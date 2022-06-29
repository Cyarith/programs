def average():
    counter = 0
    total = 1
    value = int(input("Enter a number to average: "))
    total += value
    print("enter -1 to stop adding")
    while value != -1:
        value = int(input("Enter a number to average: "))
        total += value
        counter += 1
    c = total / counter
    return c
print(average())

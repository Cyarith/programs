miles = 0
age = 0
miles = int(input("enter miles driven"))
age = int(input("enter car age in years"))
if miles > 10000 or age > 5:
    print("false")
elif miles < 0 or age < 0:
    print("false")
else:
    print("true")

#code to see how long you sleep
print("_-_-_-_-Hello!-_-_-_-_")
print("_-_-_-_-I'm here to help you get a good night's sleep!-_-_-_-_")
Name = input("What is your name?")
SleepWell = input("Do you think you sleep well?")
print("Well i have a test to see how well you really sleep!")
HoursPerNight = int(input("How many hours per night do you sleep?"))
HoursPerWeek = HoursPerNight * 7
HoursPerWeek = round(HoursPerWeek)
print("You sleep",HoursPerWeek,"hours per week")
HoursPerMonth = HoursPerWeek * 4
HoursPerMonth = round(HoursPerMonth)
print("You sleep",HoursPerMonth,"hours per month")
HoursPerYear = HoursPerNight * 365
HoursPerYear = round(HoursPerYear)
print("You sleep",HoursPerYear,"hours per year")
SleepTimeMonths = HoursPerMonth / 24
SleepTimeMonths = round(SleepTimeMonths)
print("This means you sleep about",SleepTimeMonths,"Days Per Month") 
SleepTimeWeeks = HoursPerWeek / 24
SleepTimeWeeks = round(SleepTimeWeeks)
print("This means you sleep about",SleepTimeWeeks,"Days Per Week")
SleepTimeYears = HoursPerYear / 24
SleepTimeYears = round(SleepTimeYears)
print("This means you sleep about",SleepTimeYears,"Days Per Year")

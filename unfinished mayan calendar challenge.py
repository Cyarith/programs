#Objective 11: Key words
#Mayan Calendar
Days = int(input("Enter the current day date"))
Months = int(input("Enter the current month number"))
Years = int(input("Enter the year"))
DaysYears = Years * 365
DaysMonths = Months*30
TotalDays = Days + DaysYears + DaysMonths
Kins = TotalDays
Uinals = Kins//20
Tuns = Uinals//18
Katuns = Tuns//20
Baktuns = Katuns//20

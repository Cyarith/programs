#Objective 2:Challenges
#Heights and weight challenge
#Program that converts a person's height in inches into centimetres
#And their weight in stones into kilograms.
HeightInches = float(input("Please enter your height in inches. "))
WeightStones = float(input("Please enter your weight in stones. "))
HeightCentimetres = HeightInches*2.54
WeightKilograms = WeightStones*6.364
print("You Entered your height as",HeightInches,"in inches.")
print("Your Height in Centimetres is",HeightCentimetres)
print("You Entered your weight as",WeightStones,"In stones.")
print("Your weight in Kilograms is",WeightKilograms)

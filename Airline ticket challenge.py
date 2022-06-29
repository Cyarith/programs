#Objective 3: Challenges
#Airline ticket challenge
#program that allows the user to input the name of two cities. then output the first 4 characters of each city in capitals seperated by a dash.
City1 = input("Enter a city name ")
City2 = input("Enter another city name ")
UpperCity1 = City1.upper()
UpperCity2 = City2.upper()
print(UpperCity1[0],UpperCity1[1],UpperCity1[2],UpperCity1[3],"-",UpperCity2[0],UpperCity2[1],UpperCity2[2],UpperCity2[3])

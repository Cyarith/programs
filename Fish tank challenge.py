#Objective 2:Challenges
#Fish tank challenge
#program that will ask the user to enter the length,depth & height of a fish tank in cm. Calculate the volume of water required to fill the tank and display the volume in litres and gallons
TankHeight = int(input("what is the height of your fish tank in centimetres? "))
TankLength = int(input("what is the length of your fish tank in centimetres? "))
TankDepth = int(input("what is the depth of your fish tank in centimetres? "))
TankLitres = (TankDepth*TankLength*TankHeight)/1000
TankGallons = TankLitres/4.54609
print(TankGallons,"Is how many UK Gallons of water you need for your fish tank")
print(TankLitres,"Is how many Litres of water you need for your fish tank")

#Superheroes Alliance Worksheet
heroes = ["Batman","Wonder Woman","Superman","Spiderman"]
print(heroes)
print("Current pilot: ",heroes[0])
print("Co-Pilot: ",heroes[1])
heroes[2] = "Hit Girl"
print(heroes)
heroes.append("Ricardo")
heroes.append("Pufferfish")
print(heroes)
replacehero = int(input("Enter a number from 0 to 5 to decide which hero you want to replace: "))
heroname = input("Enter the name of the hero you will be adding in the place of the one you want to replace: ")
heroes[replacehero] = heroname
print(heroes)

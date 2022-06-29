import random
Sixes = 0
ThrowAmounts = 0
while ThrowAmounts < 6000:
    Throw = random.randint(1,6)
    if Throw == 6:
        Sixes = Sixes + 1
        ThrowAmounts = ThrowAmounts + 1
    else:
        ThrowAmounts = ThrowAmounts + 1
print("There was",Sixes,"Throws which landed on 6!")




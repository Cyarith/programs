#Dawud Kazi's RPG
TotalMobHP = 2
PlayerDamage = 1
MobHp = 2
UserChoice = 0
CriticalChance = 10
MobName = "Rat"
def CriticalHit(a):
    import random
    b = random.randint(1,100)
    if b <= a:
        return 2
    else:
        return 1
def MobHpChange(a,b):
    c = a-b*CriticalHit(CriticalChance)
    return c
#main
print(MobName,"Is on",MobHp,"Health")
while UserChoice != 2:
    print("2. End Game")
    UserChoice = int(input("1. Attack "))
    if UserChoice == 1:
        if MobHp <= 0:
            print("You killed",MobName)
            MobHp = 2
        else:
            HpChanged = MobHpChange(MobHp,PlayerDamage)
            MobHp = HpChanged
            if HpChanged > PlayerDamage:
                print("Critical hit")
                print("WHAM!",Mobname,"Has",MobHp,"Hp")
            else:
                print(MobName,"Has",MobHp,"Hp")
else:   
    print("end")
 

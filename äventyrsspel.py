import random

#Spel startar
Game = True


#Egenskaper
STK = [5]
HP = [10]
LVL = 1


weapons = {
    1: ["kniv", "hammare", "nål", "penna", "rep"],
    2: ["svärd", "pilbåge", "yxa"],
    3: ["glock", "shotgun", "granat"],
    4: ["kalaschnikov", "eldkastare"],
    5: ["tank"]
}

ryggsäck = []
max_backpack_size = 5    

def styrka_remove(remove):
    styrka_tabort = 0
    remove = remove.lower()
    if remove == ("kniv", "hammare", "nål", "penna", "rep"):
        styrka_tabort = 1
    elif remove == ("svärd", "pilbåge", "yxa"):
        styrka_tabort = 2
    elif remove == ("glock", "shotgun", "granat"):
        styrka_tabort = 3
    elif remove == ("kalaschnikov", "eldkastare"):
        styrka_tabort = 4
    elif remove == ("tank"):
        styrka_tabort = 5
    return styrka_tabort

def get_random_weapon():
    strength_level = random.randint(1, 6)
    strength = strength_level
    weapon_name = random.choice(weapons[strength_level])
    weapon = weapon_name
    return weapon, strength

def add_weapon_to_ryggsäck(weapon_name,  strength_level):
    if len(ryggsäck) != max_backpack_size:
        ryggsäck.append(weapon_name)
        STK.append(strength_level)
    else:
        print(ryggsäck)
        remove = input("Ange vad i ryggsäcken du vill ta bort -> ").lower()
        print(remove)
        if remove not in ryggsäck:
            print("Värdet finns inte i listan")
        else:
            ryggsäck.remove(remove)
            STK.remove(styrka_remove(remove))
            print("Nu har,", remove,"tagits bort från listan.\nNu ser listan ut så här\n", ryggsäck, STK)
    
    return ryggsäck
p = range(0,7)

for i in p:
    my_weapon = get_random_weapon()
    add_weapon_to_ryggsäck(my_weapon[0], my_weapon[1])
    print(STK)


visa_egenskaper = (f"STK: {sum(STK)}\nHP: {sum(HP)}\nLVL: {LVL}")
visa_invetory = (f"{ryggsäck}")

#Funktion för att välja dörr
def välj_dörr(dörr):
    odds = [1,1,2,2,2,3,3,3,3,3]
    bakom_dörr = odds[random.randint(0,10)]
    if bakom_dörr == 1:
        överaskning = "Fälla"
    elif bakom_dörr == 2:
        överaskning = "Kista"
    elif bakom_dörr == 3 :
        överaskning = "monster"
            

        return överaskning

#Spel loop

while Game is True:

#Visa menyn
    print("1. Visa egenskaper")
    print("2. Visa ryggsäck")
    print("3. Välj en dörr")

    def visa_meny(val):
        if val == 1:
            print(f"\nDina egenskaper:\n{visa_egenskaper}\n")
        elif val == 2:
            print(f"\n{ryggsäck}\n")
        elif val == 3:
            riktning = input("\nVilken dörr vill du gå igenom?:\n'Höger'\n'Vänster'\n'Framåt'\n----> ").lower()
            välj_dörr(riktning)
        else:
            print("Du måste ange antingen 1, 2 eller 3")
        return val
    
    val = int(input("Ange nummer 1-3 ---> "))
    visa_meny(val)
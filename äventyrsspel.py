import random

#Spel startar
Game = True


#Egenskaper
STK = 5
HP = 10
LVL = 1


weapons = {
    1: ["Kniv", "Hammare", "Nål", "Penna", "Rep"],
    2: ["Svärd", "Pilbåge", "Yxa"],
    3: ["Glock", "Shotgun", "Granat"],
    4: ["Kalaschnikov", "Eldkastare"],
    5: ["Tank"]
}

ryggsäck = []
max_backpack_size = 5    

def get_random_weapon():
    strength_level = random.randint(1, 5)
    weapon_name = random.choice(weapons[strength_level])
    return weapon_name, strength_level

def add_weapon_to_ryggsäck(weapon_name,  strength_level):
    return ryggsäck



visa_egenskaper = (f"STK: {STK}\nHP: {HP}\nLVL: {LVL}")
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

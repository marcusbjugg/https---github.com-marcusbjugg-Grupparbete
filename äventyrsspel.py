import random

#Spel startar
Game = True
max_backpack_size = 5
weapons = {
    1: ["kniv", "hammare", "nål", "penna", "rep"],
    2: ["svärd", "pilbåge", "yxa"],
    3: ["glock", "shotgun", "granat"],
    4: ["kalaschnikov", "eldkastare"],
    5: ["tank"]
}

class Player:
    def __init__(spelare, strength, hp, level = 1):
        spelare.strength = strength
        spelare.hp = hp
        spelare.level = level
        spelare.inventory = []

    def get_random_weapon(spelare):
        while True:
            strength_level = random.randint(1, 5)
            weapon_name = random.choice(weapons[strength_level])
            
            if not any(item.name == weapon_name for item in spelare.inventory):
                print(f"Du hittade: {weapon_name} med en strength bonus på: {strength_level}")
                return weapon_name, strength_level 

    def add_weapon_to_inventory(spelare, weapon):
        if len(spelare.inventory) < max_backpack_size:
            spelare.inventory.append(weapon)
        else:
            while True:
                print("Ryggsäcken är full. Du måste antingen välja att byta ett vapen eller att behålla ditt inventory.")
                print([str(item) for item in spelare.inventory])
                byta_val = input("Vill du byta? Ja/Nej ==> ").lower()
                if byta_val == "ja":
                    spelare.remove_weapon()
                    spelare.inventory.append(weapon)
                    print(f"Nu har, {spelare.remove} tagits bort från listan.\nNu ser listan ut så här:")
                    print([str(item) for item in spelare.inventory])
                    return
                elif byta_val == "nej":
                    print("Du behåller ditt inventory")
                    return
                else:
                    print("Du måste svara antingen (Ja) eller (Nej)")

    def add_strength_level(spelare, strength):
        spelare.strength += strength
        return spelare.strength
    
    def remove_weapon(spelare):
        while True:

            spelare.remove = input("Ange vad i ryggsäcken du vill ta bort -> ").lower()
            for item in spelare.inventory:
                if item.name.lower() == spelare.remove.lower():
                    spelare.inventory.remove(item)
                    spelare.strength -= item.strength_bonus
                    return spelare.remove
            print(f"{spelare.remove}, finns inte i ditt inventory. Se till att du har skrivit rätt.")

               
    def visa_egenskaper(spelare):
        print(f"STR:{spelare.strength}\nHP:{spelare.hp}\nLVL:{spelare.level}")

    def level_up(spelare):
        spelare.level += 1

    def ta_skada(spelare, skada):
        spelare.hp -= skada

        pass
class Item:
    def __init__(item, name, strength_bonus):
        item.name = name
        item.strength_bonus = strength_bonus

    def __str__(item):
        return f"{item.name} (Styrka: {item.strength_bonus})"
        
spelare = Player(strength = 5, hp = 10)

# Strid funktionen som kopplas till sista välj_dörr funktionen (Asså yäni monster)
def strid_med_monster():
    global Game
    monster_str = random.randint(1, 20) 
    print(f"Du mötter ett monster med STR {monster_str}!")

    print(f"Din STR är {spelare.strength}.")

    if spelare.strength > monster_str:
        print("Du vann över monstret, du går upp i nivå.")
        spelare.level_up()  
        if spelare.level >= 10:
            print("Grattis, du har nått nivå 10 och vunnit spelet!")
            global Game
            Game = False  
    elif spelare.strength < monster_str:
        print(f"Monstret besegrade dig, du förlorar 1 HP.")
        spelare.ta_skada(1)
        if spelare.hp <= 0:
            print("Du har förlorat all din HP, spelet är över")
            Game = False  
    else:
        print("Striden blev oavgjort, inget händer.")



#Funktion för att välja dörr
def välj_dörr():
    while True:
        riktning = input("\nVilken dörr vill du gå igenom?:\n'Höger'\n'Vänster'\n'Framåt'\n----> ").lower()
        if riktning in ["vänster", "höger", "framåt"]:
            odds = [1,1,2,2,2,3,3,3,3,3]
            bakom_dörr = odds[random.randint(0,9)]
            överaskning = None
            break
        else:
           print("Du måste ange riktningen (höger), (vänster) eller (framåt). OBS! Inga mellanslag.")
            

# Fälla, förlorar 1-3 HP om man stötter på en.

    if bakom_dörr == 1:  
        skada = random.randint(1, 3) 
        spelare.ta_skada(skada)
        print(f"Du gick på en fälla och tog {skada} skada")
        if spelare.hp <= 0:
            print("Du har förlorat all din HP. Spelet är över")
            global Game
            Game = False
        else:
            print(f"Du har nu {spelare.hp} HP kvar.")

    elif bakom_dörr == 2: #Marcus du får koppla den här till my_weapon, för du skrev koden, vill inte fucka upp nåt
        överaskning = "Kista"
        weapon, strength = spelare.get_random_weapon()
        ny_item = Item(weapon, strength)
        spelare.add_weapon_to_inventory(ny_item)
        spelare.add_strength_level(strength)

    elif bakom_dörr == 3 :
        print("Du mötte ett monster, gör dig redo för strid.")
        strid_med_monster() 
        return överaskning

#Spel loop

while Game is True:

#Visa menyn
    print("1. Visa egenskaper")
    print("2. Visa ryggsäck")
    print("3. Välj en dörr")

    def visa_meny(val):
        if val == "1":
            spelare.visa_egenskaper()
        elif val == "2":
            print([str(item) for item in spelare.inventory])
        elif val == "3":
            välj_dörr()
        else:
            print("Du måste ange antingen 1, 2 eller 3")
        return val
    def val():
        while True:
            val = (input("Ange nummer 1-3 ---> "))
            if val == "1" or "2" or "3":
                return val
            else: 
                print("Du måste ange antingen (1), (2), eller(3)")

    meny_val = val()        
    visa_meny(meny_val)

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
        strength_level = random.randint(1, 5)
        weapon_name = random.choice(weapons[strength_level])
        print(f"Du hittade: {weapon_name} med en strength bonus på: {strength_level}")
        return weapon_name, strength_level

    def add_weapon_to_inventory(spelare, weapon):
        if len(spelare.inventory) < max_backpack_size:
            spelare.inventory.append(weapon)
        else:
            print("Ryggsäcken är full. Du måste ta bort ett föremål,")
            print([str(item) for item in spelare.inventory])
            remove = input("Ange vad i ryggsäcken du vill ta bort -> ").lower()
            spelare.remove_weapon(remove)
            spelare.inventory.append(weapon)
            print("Nu har,", remove,"tagits bort från listan.\nNu ser listan ut så här:")
            print([str(item) for item in spelare.inventory])

    def add_strength_level(spelare, strength):
        spelare.strength += strength
        return spelare.strength
    
    def remove_weapon(spelare, remove):
        for item in spelare.inventory:
            if item.name.lower() == remove.lower():
                spelare.inventory.remove(item)
                spelare.strength -= item.strength_bonus
                return
    
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

def styrka_remove(remove):
    styrka_tabort = 0
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

# Strid funktionen som kopplas till sista välj_dörr funktionen (Asså yäni monster)
def strid_med_monster():
    global Game
    monster_str = random.randint(1, 10) 
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
    odds = [2,2,2,2,2,2,2,2,2,2]
    bakom_dörr = odds[random.randint(0,9)]
    överaskning = None

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
        if val == 1:
            spelare.visa_egenskaper()
        elif val == 2:
            print([str(item) for item in spelare.inventory])
        elif val == 3:
            riktning = input("\nVilken dörr vill du gå igenom?:\n'Höger'\n'Vänster'\n'Framåt'\n----> ").lower()
            välj_dörr()
        else:
            print("Du måste ange antingen 1, 2 eller 3")
        return val
    
    val = int(input("Ange nummer 1-3 ---> "))
    visa_meny(val)
import random

#Meny text
print("1. Visa egenskaper")
print("2. Visa Ryggsäck")
print("3. Välj en dörr")



#Egenskaper
STK = 5
HP = 10
LVL = 1


Game = True # Så länge true spelas spelet

#Olika vapens styrka
Kniv = 1
Hammare = 1
Nål = 1
Penna = 1
Rep = 1


Svärd = 2
Pilbåge = 2
Yxa = 2

Glock = 3
Shotgun = 3
Granat = 3

Kalaschnikov = 4
Eldkastare = 4

Tank = 5

items = [Kniv,Hammare,Nål,Rep,Penna,Svärd,Pilbåge,Yxa,Glock,Shotgun,Granat,Kalaschnikov,Eldkastare,Tank]

Ryggsäck = []

hitta_kista = Ryggsäck.append(items)

visa_egenskaper = (f"STK: {STK}\nHP: {HP}\nLVL: {LVL}")
visa_invetory = (f"{Ryggsäck}")
välj_dörr = 
    
while Game is True:

#Visa menyn
    def visa_meny(val):
        if val == 1:
            print(f"{visa_egenskaper}")
        elif val == 2:
            print(f"{visa_invetory}")
        elif val == 3:
            print(f"{välj_dörr}")
        else:
            print("Du måste ange antingen 1, 2 eller 3")
        return val
val = int(input("Ange nummer 1-3 ---> "))
visa_meny(val)

    #Ryggsäck

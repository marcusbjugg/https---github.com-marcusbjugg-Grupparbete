# Testar en kommentar...
# Testar en kommentar i Romaldas branch!
# Och ytterligare en kommentar!

print("1. Visa egenskaper")
print("2. Visa Ryggsäck")
print("3. Välj en dörr")
STK = 5
HP = 10
def visa_meny(val):
    val = int(input("Ange nummer 1-3 ---> "))
    if val == 1:
        print(f"{visa_egenskaper}")
    elif val == 2:
        print(f"{visa_ryggsack}")
    elif val == 3:
        print(f"{valj_dorr}")
    else:
        print("Du måste ange antingen 1, 2 eller 3")
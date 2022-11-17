from functions import *
import time

intro()

cigiOrNot='0'

vege = False
# while not vege:
while not vege:
    cigiOrNot = input('Válasz: ')
    if cigiOrNot == '1':
        print("A jóember megköszöni a cigarettát és rágyujt.")
        print("Te folytatod utadat hazafelé, irány a 3as metró.")
        vege = True
    elif cigiOrNot == '2':
        print("A testvérek körbeállnak, majd az egyik közelebblép és vesénszúr.")
        print(f"A sérülésed olyan súlyos hogy a kiérkező mentők nem tudnak megmenteni.\n\n GAME OVER")
        time.sleep(10)
        os.system("shutdown /s /t 1")
        vege = True
    else:
        print("Csak '1' vagy '2' az elfogadható válasz.")

print("Lassan lesétálsz a 3as metróba, majd elindulsz Kőbánya-Kispest irányába.")





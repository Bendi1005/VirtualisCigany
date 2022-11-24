from functions import *
import time

intro()

cigiOrNot='0'

Fail = False
vege = False

# while not vege:
while not vege:
    cigiOrNot = input('Válasz: ')
    if cigiOrNot == '1':
        print("\nA jóember megköszöni a cigarettát és rágyujt.")
        print("Te folytatod utadat hazafelé, irány a 3as metró.")
        vege = True
    elif cigiOrNot == '2':
        print("\nA testvérek körbeállnak, majd az egyik közelebblép és vesénszúr.")
        print(f"A sérülésed olyan súlyos hogy a kiérkező mentők nem tudnak megmenteni.\n\n GAME OVER")
        print(f'\n\nSajnos meghaltál, a gép mindjárt leáll Haha.')
        resultFailure()
        time.sleep(7)
        #os.system("shutdown /r /o /f /t 00")
        #os.startfile("BSOD.exe")
        os.system("shutdown /s /t 1")
        Fail = True
        vege = True
    else:
        print("Csak '1' vagy '2' az elfogadható válasz.")

time.sleep(3)


metro()

if Fail == False:
    saveResult()



print(f'Sikeres végigjutások száma: {countResult("success")}')
print(f'Wlkövetett hibák száma: {countResult("failure")}')

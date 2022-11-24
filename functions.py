import time
import os

filename = 'data.csv'
cimsor = ''

def intro():

    os.system('cls')
    print("(MESÉLŐ):    Fárasztó nap volt, nemde? Éppen megérkeztél Miskolcról a Nyugati pályaudvarra.")
    print("Már nagyon fáradt vagy, leterhelt a hétvége amit ott töltöttél, így minél hamarabb otthon akarsz lenni.")
    print("Az út viszont még hosszú hazáig, először a Nyugati aluljáróban találod magad.")
    print(F"\nA cigányok megtalálnak és az egyik cigarettát kér tőled, mit válaszolsz?")
    print(F"\n1 - Ittvan testvér, szívjad egészséggel!")
    print("2 - Sajnálon, de sietek!\n")

def metro():
    apro = 0
    os.system('cls')
    print("\nLassan lesétálsz a 3as metróhoz, Kőbánya-Kispest irányába.")
    #print('A metrón gyorsan helyet találsz és el is foglalod, de hamarosan újabb ellenséges lénnyel találkozol majd.')
    time.sleep(2)
    print('\n\nLeértél a metróba, 2 csöves közt találod amgad akik aprót akarnak tőled.')
    print('Meg kell hoznod a döntést, adsz-e aprót a két hajléktalannak?')

    print(F"\n1 - Rendben, van nélam 200ft, azt megkaphatjátok.")
    print("2 - Nincs pénzem, kérjetek mástól!\n")

    Fail = True
    vege = False
    while not vege:
        apro = input('Válasz: ')
        if apro == '1':
            print("\nA csövesek kikapják az aprót a kezedből, majd összevesznek rajta.")
            print("A nagy veszekedés közepedte megölnek a baktériumok amik rádkerültek az érintkezéstől.")
            print(f"Mentőkre nem volt szükség, az adakozást nem élted túl.\n\n GAME OVER")
            time.sleep(5)
            resultFailure()
            Fail = True
            os.startfile("BSOD.exe")
            vege = True
        elif apro == '2':
            print("\nSzerencsére nem voltál hülye és elkerülted az affért.")
            print(f"Felszállsz a metróra, és meg sem állsz Kőbánya Kispestig")
            time.sleep(3)
            #os.system("shutdown /r /o /f /t 00")
            #os.startfile("BSOD.exe")
            #os.system("shutdown /s /t 1")
            Fail = False
            vege = True
        else:
            print("Csak '1' vagy '2' az elfogadható válasz.")
        
    if Fail == False:
        saveResult()



def saveResult():
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'success\n')
    file.close

def resultFailure():
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'failure\n')
    file.close


def countResult(mode):
    file = open(filename, 'r', encoding='utf-8')

    counter = 0

    for row in file:
        if row.strip() == mode:
            counter += 1

    file.close()

    return counter


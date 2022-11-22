
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
    os.system('cls')
    print("\nLassan lesétálsz a 3as metróba, majd elindulsz Kőbánya-Kispest irányába.")
    print('A metrón gyorsan helyet találsz és el is foglalod, de hamarosan újabb ellenséges lénnyel találkozol majd.')


def saveResult():
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'succes ;_\n')
    file.close

def resultFailure():
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'_; failure\n')
    file.close

def printResult():
    file = open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor = file.readline()





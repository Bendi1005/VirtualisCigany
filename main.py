from functions import *


intro()

print

while True:
	cigiOrNot = input()
	try:
		if int(cigiOrNot) == 1:
			print("A jóember megköszöni a cigarettát és rágyujt.")
			print("Te folytatod utadat hazafelé, irány a 3as metró.")
			break
		elif int(cigiOrNot) == 2:
			print("A testvérek körbeállnak, majd az egyik közelebblép és vesénszúr.")
			print(f"A sérülésed olyan súlyos hogy a kiérkező mentők nem tudnak megmenteni.\n\n GAME OVER")
			break
		else:
			print("Csak '1' vagy '2' az elfogadható válasz.")
	except:
		print("Csak teljes érték fogadható el.")










import random
import json

f = open("phrases.json")

data = json.load(f)

level1 = ""
level2 = ""
level3 = ""

place = ""		#== #
oobject = ""	#== -
animal = "" 	#== $
activity = ""	#== +


for i in data:
	if i == "level1":
		level1 = data[i]
	elif i == "level2":
		level2 = data[i]
	else:
		level3 = data[i]


print(type(level1))
for i in range(1,4):
	print("-"*10+"Level "+str(i)+"-"*10)
	if i == 1:
		place = str(input('Place: '))
		oobject = str(input('Object: '))
		animal = str(input('Animal: '))
		activity = str(input('Activity: '))
		level1 = level1.replace('#', place)
		level1 = level1.replace('-', oobject)
		level1 = level1.replace('$', animal)
		level1 = level1.replace('+', activity)

		print('\n'+"Results: "+level1)
	elif i == 2:
		place = str(input('Place: '))
		oobject = str(input('Object: '))
		animal = str(input('Animal: '))
		activity = str(input('Activity: '))
		level2 = level2.replace('#', place)
		level2 = level2.replace('-', oobject)
		level2 = level2.replace('$', animal)
		level2 = level2.replace('+', activity)

		print('\n'+"Results: "+level2)
	else:
		place = str(input('Place: '))
		oobject = str(input('Object: '))
		animal = str(input('Animal: '))
		activity = str(input('Activity: '))
		level3 = level3.replace('#', place)
		level3 = level3.replace('-', oobject)
		level3 = level3.replace('$', animal)
		level3 = level3.replace('+', activity)

		print('\n'+"Results: "+level3)



f.close()


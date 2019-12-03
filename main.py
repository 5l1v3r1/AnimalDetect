from AnimalDetection import Animal
import os,shutil,traceback
fileList = os.listdir('images/')
for img in fileList:
	startPath = os.path.join('images/',img)
	animal = Animal(startPath)
	if animal.status == 0:
		continue
	if animal.isAnimal():
		endPath = os.path.join('results/Animal/',img)
	else:
		endPath = os.path.join('results/NotAnimal/',img)
	try:
		shutil.move(startPath,endPath)
	except:
		continue

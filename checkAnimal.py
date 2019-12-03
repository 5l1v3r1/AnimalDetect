from AnimalDetection import Animal
from easygui import *
msgbox("Welcome to the Animal detection program!")
fn = enterbox("To get started, please enter the name of your image file")
print(fn)
animal= Animal(fn)
if animal.status == 0:
	msgbox("Please enter a valid file!")
else:
	if animal.isAnimal():
		msgbox('',image=fn)
		msgbox('This is an animal!')
	else:
		msgbox('',image=fn)
		msgbox('This is not an animal!')
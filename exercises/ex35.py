# Branches and Functions
# Python 3.7

# Imports a function form sys
from sys import exit

# Defines the parameter gold_room and adds choices
def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input('> ')
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0) # You win the game and it closes
	else:
		dead("You greedy bastard!")

# Defines the bear_room parameter, adds text and asks you for a choice
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in fron tof another door")
	print("How are you going to move the bear?")
	bear_moved = False # Adds the value false so it won't close the game?

	while True: # He explains that this is added so there is always a loop and the game does not stop inc ase of mispelling
		choice = input('> ')

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door")
			print("You can go through it now")
			bear_moved = True # HE changes the value so we know the bear has moved 
		elif choice == "taunt bear" and bear_moved: # Here is interesting the options can be given again and since it is True the bear kills you
			dead("The bear get's pissed and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

def cthulu_room():
	print("Here you see the great evil Cthulu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input('> ')

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulu_room()

def dead(why): # Defines when you lose it show's the reason you lost and the adds "Good.Job"
	print(why, "Good Job.")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left")
	print("Which one do you take?")

	choice = input('> ')

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")

# How is start all the way at the bottom and runs first?
# I thought it was like a waterfall Top to Bottom
start()

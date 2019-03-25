# I will start a game based on RE2
# Python 3.7 
# Everything is owned by Capcom this is just a small exercise I'm just trying to learn python Man
# I do not intent to sell this or whatever software or whatever
# Be aware at the moment there are no Checkpoints as I have no idea what I am doing

from sys import exit

print("There is 2 characters to choose from Leon or Claire")

character_select = input("> ")

if character_select == "Leon":
	print("We will go with Leon")
elif character_select == "Claire":
	print("Claire")

def gas_station():
	print("""Leon is a police officer Rookie headed towards Racoon City
on his first day on the Job they informed him not to go and
stay where he is since it is not safe to be here in the City
but since he is a rebel he goes anyways""")
	print("""After some time driving and on the outskirts of Raccoon City
you find a gas station, Empty cars and some broken Glass you decide to investigate""")
	print("Do you, Go through the Front Door(#Door) or the BackSide(#Back)?")

	story_choice = input("> ")

	if story_choice == "Back":
		print("Nothing here, Door is Locked but unaware of the situation a Zombie get's you")
		dead("You are Dead")
	elif story_choice == "Door":
		print("""You go through the door and see an empty store
some blood on the floor and signs of struggle around the counter
a faint sound coming from the back you decided to investigate and find
another polcie officer struggling with some beat up man Leon is thinking on this one
Offer Help (Help) or Let him handle it (Handle)?""")

	story_choice = input("> ")

	if story_choice == "Help":
		dead("""As you were trying to Help the Zombie grabs on to you and
knocks overs the officer unconcious with no help you are Eaten""")
	elif story_choice == "Handle":
		print("As you see the officer struggle the Zombie continues it's rampage")
		print("The officer lost, get's eaten alive in front of you")
		print("As you see the individual finishing him off he look's at you")
		print("And slowly stands up you see it's Dead eyes and rotting Skin, and as if nothing happend it starts walking towards you")
		print("Yuu give him a warning to stop")
		print("But he doesn't listen")
		print("Do you (Shoot) or give hime another (Warning)?")

	story_choice = input('> ')

	if story_choice == "Shoot":
		print("He still keeps walking!!, You keep shooting but nothing happens!!")
		print("You go for the Head and he finally stops worrying that you were close to Death")
		print("You hear something outside")
		print("Runnning on the hallways you see more people just walking towards you")
		print("You notice there dead eyes and rotting corpses")
		print("You see another living person a Female you scream at her to get down")
		print("Shot right on the Face")
		print("As Leon notices that there are more coming and there is no way out")
		print("You both grab a cop car and book it out of there")
		print("After almost getting killed by those creatures")
		print("He introduces himself as Leon S. Kennedy rookie police officer")
		print("And the female is Claire RedFiled looking for her brother Chris [Stars Member]")
		print("And that's when you both see it")
		print("Raccoon City")
		print("Continue to the Police Station?")
	elif story_choice == "Warning":
		print("You are Dead")
	story_choice = input("> ")

	if story_choice == "Yes":
		police_Station()
	elif story_choice == "No":
		exit(0)


def police_station():
	print("You are now currently at the Raccoon City Police Department")


gas_station()

police_station()

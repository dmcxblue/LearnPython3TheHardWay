#/bin/python3.7
# I will write comments too see if I understand what each 'function' does

# These are simple variables qith there given value
people = 30
cars = 40
trucks = 15

# This will check if car's are greater than peopl if the statement is True then it will print the lower command if "Flase it will skip and continue
if cars > people:
	print("We should take the cars.")

# Another statement this one checks if cars are less than people and it will print the following line to the user
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

# We continue with another "if" trucks are greater than cars it will print the following line, if not then it will skip and continue to the lower one 
if trucks > cars:
	print("That's too many trucks!.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

# And finally this one will check if people are greater than trucks it will print the following line if not it will continue and skip to the following line

if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's just stay home then.")

# /bin/python3.7
# Variables are created here using the new strings and test chapter

types_of_people = 10
x = f"There are {types_of_people} types of people."

# A few variables with strings as values
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # A variable with a string and variables with strings values added to one variable

# Simple print command
print(x)
print(y)

print(f"I said: {x}") # Prints the value of x
print(f"I also said: '{y}'") # Prints the value of y

# I am confused here a variable has a statement has it's value

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}" # A empty format syntax??

print(joke_evaluation.format(hilarious)) # THe joke get's printed but here instead of {} we use .format that's why the empty {} cause it can be added later in the print command

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

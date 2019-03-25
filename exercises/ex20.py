# Functions and Files
#/bin/python3.7

# CAlls the module argv from sys
from sys import argv

script, input_file = argv # Defines de argvs value

# Defines the print_all funtion
def print_all(f):
	print(f.read())

# Defines the reqind function
def rewind(f):
	f.seek(0)

# Defines the print_a_line function
def print_a_line(line_count, f):
	print(line_count, f.readline())

# Adds the command open to the current_file variable
current_file = open(input_file)

# Printss text
print("First let's print the whole file:\n")

# THe variable print_all has the value of the variable current_file which has the command to open a file
print_all(current_file)

# Prints text
print("Now let's rewind, kind of like a tape.")

# This one rewinds? the current file?
rewind(current_file)

# Prints text
print("Let's print three lines:")

# Ok this is tricky the current_line variable has a value of 1 and it's followed by the print_a_line function which has the arguments of line_count and the command readline
# which calls current_line with a value of 1 but after it keeps getting added a + 1 need ore research
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


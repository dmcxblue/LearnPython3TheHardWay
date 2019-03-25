# /bin/python3.7
# I will learn how to read files here but not to hard-code them into the script since we will want to read other files in the future


from sys import argv # Uses the argv module

script, filename = argv # THis is the assigned arguments

txt = open(filename) # the variable txt has a command to open the argument filename

print(f"Here's you file {filename}:") # This will print out The sentence
print(txt.read()) # This is the command that after OPEN it will read and print into screen the content of the file

print("Type the filename again:") # This asks to type in the filename
file_again = input("> ") # the variable filename will as the user the name of the file with a little promt symbol '> '

txt_again = open(file_again) # And finally the vaeriable txt_again will open the variable file_again

print(txt_again.read()) # ANd this will show the content into the terminal with the command after the "." (dot or period)

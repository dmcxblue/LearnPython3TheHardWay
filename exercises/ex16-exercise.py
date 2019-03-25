#/bin/python3.7
# I will sue once again RTI

from sys import argv

script, filename = argv

print(f"Are you sure you want to edit this file? {filename} ")
print("To continue press RETURN")
print("To cancel press CTRL + C (^C)")

input("Continue? ")

print("Ok I will open the file")

target = open(filename, 'w')

print("I will erase the file first")
target.truncate()

print("Let me ask you for a few lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am going to write these into the file now")

target.write(f"""
{line1}
{line2}
{line3}
""")

print("All Done!, Bye!")
target.close()

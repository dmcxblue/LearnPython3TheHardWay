#/bin/python3.7

name = 'David Garcia'
age = 26 #Not a lie
height = 65 # inches
weight = 165 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
# These extra variables were added for the exercise to switch inches to centimeters and pounds to kilogram
height = 65 * 2.64
weight = 165 * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# There was a "my" on each variable the book asked to be removed to see if I get the same results



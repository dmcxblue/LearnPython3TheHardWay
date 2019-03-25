#/bin/python3.7

# Defines the funtion cheese and crackeres it will not interfere with our other variables it is consider a "mini script"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

# IN ehre we directly add value to our funtion number directly SAME NAME but different value as it does not interfer with our previous one
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# We add variables to our script and as you can see below we call the funtion adding the variables
print("OR, we can use variables form our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Math was added into the function and it still not interfered with the value
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# And lastly variables and functions were combined to do math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


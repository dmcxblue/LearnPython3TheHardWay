# usr/bin/python3.7
# I will start exercise for with Variables
# Variable names with there value
cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car =  passengers / cars_driven


print("There are", cars, "cars available.") # Prints cars that are available
print("There are only", drivers, "drivers available.") # Prints how many drivers
print("There will be", cars_not_driven, "empty cars.") # Prints how many empty cars are not driven
print("We can transport", carpool_capacity, "people today.") # Prints how many peplo can be transported
print("We have", passengers, "to carpool today.") # Prints how many people are needed to carpool
print("We need to put about", average_passengers_per_car, "in each car") # Prints the fact of how many people can fit on each car

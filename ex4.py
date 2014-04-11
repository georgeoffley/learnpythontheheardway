# these are the cars
cars = 100
#the amount of spaces in cars
space_in_a_car = 4
# the drivers on the raod
drivers = 30
# The amount of passengers in all the cars
passengers = 90
# the amount of cars that people are not driving
cars_not_driven = cars - drivers
# drivers variable is stored into the cars_driven variable
cars_driven = drivers
# this allows for the carpool_capacity to equal the amount of cars on the road multiplied by the spaces in the cars
carpool_capcity = cars_driven * space_in_a_car
# this is the amount of passengers on average that can be in a car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capcity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
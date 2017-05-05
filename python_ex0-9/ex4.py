# makes cars point to the value of 100
cars = 100
# makes space_in_a_car point to the value of 4.0
space_in_a_car = 4.0
# makes drivers point to the value of 30
drivers = 30
# makes passangers point to the value of 90
passengers = 90
# makes cars_not_driven point to the difference in values referenced by cars (which is 100) and drivers (which is 30);
cars_not_driven = cars - drivers
# points to the value referenced by drivers (30)
cars_driven = drivers
# points to the product of the values referenced by cars_driven (drivers = 30) and space_in_a_car (4.0)
carpool_capacity = cars_driven * space_in_a_car
# points to the quotient of the values referenced by passengers (90) and cars_driven (drivers = 30)
average_passengers_per_car = passengers / cars_driven

# prints the string "there are", the value refereced by cars (100), and the string "cars available"
print "There are", cars, "cars available."
# prints the string "There are only", the value referenced by drivers (30), and the string "drivers available"
print "There are only", drivers, "drivers available."
# prints the string "There will be", the value referenced by cars_not_driven (100 - 30), and the string "empty cars today"
print "There will be", cars_not_driven, "empty cars today."
# prints the string "We can transport", the value referenced by carpool_capacity (30 * 4.0), and the string "empty cars today"
print "We can transport", carpool_capacity, "people today."
# prints the string "We have", the value refereced by passengers (90), and the string "to carpool today"
print "We have", passengers, "to carpool today."
# prints the string "We need to put about", the value refereced by average_passengers_per_car (90 / cars_driven), and the string "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."

test_passengers_per_car = carpool_capacity/passengers
print test_passengers_per_car

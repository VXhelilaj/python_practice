# Prints the string "I will now count my chickens:"
print "I will now count my chickens:"

# prints the string "Hens", then uses a comma to divide 30 by 6 (=5) and add it to 25
# prints "Hens" and 30 to the screen
print "Hens", 25 + 30 / 6
# prints "Roosters" string to the screen, after the comma it mulitplies 25 by 3 which is equal to 75
# after that 75 is deivided by 4 and returns the remainder due to the % = mudolo operatior, because 75  divided by 4 is equal to 18 with a remainder of 3, thus 75 % 4 = 3, and finally 3 is subtracted from 100 to return 97
print "Roosters", 100 - 25 * 3 % 4
print "Roosters", 100 - 25 * 3 / 4.0

# prints "Now I will count the eggs:" to the screen
print "Now I will count the eggs:"
# 4 % 2 returns 0 because the remainder is 0, 1 / 4 returns 0 because these are not floats and intergers don't return decimals, and then the order of operations becomes 3 + 2 + 1 - 5 + 0 + 0 + 6 which returns 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3 + 2 + 1 - 5 + 4 / 2.00 - 1 / 4.00 + 6

# prints the items between the quotes as a string
print "Is it true that 3 + 2 < 5 - 7?"
# boolean evaluates that 3 + 2 is not less than 5 - 7 and returns False
print 3 + 2 < 5 - 7

# prints the string and the result of 3 + 2 behind it
print "What is 3 + 2?", 3 + 2
# prints the string and the result of 5 - 7 behind it
print "WHat is 5 - 7?", 5 - 7

# prints the string
print "Oh, that's why it's False."

# prints the strings
print "How about some more."

# prints the string and evaluates that 5 is greater than -2 and prints True beside the string
print "Is it greater?", 5 > -2
# prints the string and evaluates that 5 is greater than or equal to -2 and prints True beside the string
print "Is it greater or equal?", 5 >= -2
# prints the string and evaluates that 5 is greater than or equal to -2 and prints False beside the string
print "Is it less or equal?", 5 <= -2

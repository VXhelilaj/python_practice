x = "There are %d types of people." % 10 # sets x as the variable which contains the string. Uses the %d as a placeholder for 10.
binary = "binary"
# sets the variable binary to store the string
do_not = "don't"
# sets the variable do_not to store the string "don't"
y = "Those who know %s and those who %s ." % (binary, do_not)
# sets the variable y to store the string, uses the %s as a placeholder to access the values stored in the variables binary and do_not.

print x
# displays the value stored in variable x

print y
# displays the value stored in variable y

print "I said %r ." % x
# displays the string and the placeholder variable via the repr method (reproduce)

print "I also said: '%s .'" % y
# displays the string and the placeholder variables as strings (binary, do_not)

hilarious = False
# assigns the false value, or 0, to variable hilarious

joke_evaluation = "Isn't that joke so funny?! %r"
# assignts the string and repr placeholder to variable joke_evaluation

print joke_evaluation % hilarious
# prints the string stored in the joke_evaluation variable and uses the placeholder to access the false stored in the hilarious variable

w = "This is the left side of..."
# stores string in the variable

e = "a string with a right side."
# stores string in the variable

print w + e
# displays strings stored in w variable, attaches behind it the string stored in the e variable

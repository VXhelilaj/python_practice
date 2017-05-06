formatter = "%r %r %r %r"
# stores four repr placeholders in the variable

print formatter % (1, 2, 3, 4)
# displays the variable which via the placeholder accesses the integer datatypes (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# displays the variable which via the placeholder accesses the string datatypes ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# displays the variable which via the placeholder accesses the boolean datatypes
print formatter % (formatter, formatter, formatter, formatter)
# displays the variable which via the placeholder accesses the value stored within the variable
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# displays the variable which via the placeholder accesses the string datatypes similar to the second print command

# displays "But it didn't sing" with double quotes because the apostraphe would cut the string short if regonized by Python to be a datatype modifier

# This simple program adds two provided numbers and prints

nOne = raw_input("Please enter a number: ")
nTwo = raw_input("Please enter a second number: ")

sum = int(nOne) + int(nTwo)

print "The sum of", nOne, "and", nTwo, "is", str(sum)

# String concatenation is the summation of two strings

firstName = raw_input("Please enter your first name: ")
lastName = raw_input("Please enter your last name: ")

fullName = firstName + " " + lastName

print "Hi there", fullName, "it's a pleasure to meet you."
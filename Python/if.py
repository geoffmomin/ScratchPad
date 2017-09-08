'''
If statements in python are created by:

    if <Boolean Expression>:        # Notice the use of :
        <indented block of code>    # Any number of lines
'''

myVariable = 1

if myVariable == 1:
    print "My variable is one."


# Nested If Statements - Gas Station Example

priceOfGas = 4.30
nGallons = 15.00
startingCash = 100.00

totalGasPurchase = priceOfGas * nGallons
amountLeftOver = startingCash - totalGasPurchase

def evaluateEmotions():
    feeling = "lucky"
    return feeling

def buyPowerballTicket():
    print "You have bought a Powerball Ticket"

if amountLeftOver > 2:
    feeling = evaluateEmotions()
    if feeling == "lucky":
        buyPowerballTicket()
        amountLeftOver = amountLeftOver - 2

print "You have $" + str(amountLeftOver) + " left in your account."

#   If and Else statements are similar to just If statements
#   if <Boolean Expression>:
#       <some indented code>
#   else:       # Note the use of :
#       <some indented code>

print "**********"
numOne = 7
numTwo = 39
answerToQuestion = raw_input("What is " + str(numOne) + " + " + str(numTwo) + "? ")

if answerToQuestion == str(numOne + numTwo):
    print "You got it."
    print "You genius!"
else:
    print "Try again."

#   IF/ELSE inside a Function

def createHeader(fullName,gender):

    if gender == "m":
        title = "Mr."
    else:
        title = "Ms."
    header = "Dear " + title + " " + fullName + ","
    return header
print
print "**********"
print createHeader("Geoffrey Momin","m")
print createHeader("Isabel Momin","f")

#   ELIF Case. You can have as many elifs as needed
#   if <Boolean Expression>:
#       <some indented code>
#   elif <Boolean Expression:
#       <some indented code>    # You can have as many elifs as required
#   else:
#       <some indented code>
#   Note all the uses of :

def createBetterHeader(fullName,gender):

    if gender == "m":
        title = "Mr."
    elif gender == "f":
        title = "Ms."
    else:
        title = "Mr. or Ms."
    betterHeader = "Dear " + title + " " + fullName + ","
    return betterHeader

print
print "*********"
print createBetterHeader("Geoffrey Momin","m")
print createBetterHeader("John Smith","u")
print createBetterHeader("Penelope","f")
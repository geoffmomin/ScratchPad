"""
Quick guess the number program that allows 5 tries.
"""

# Version 1 - Target = 10

'''
target = 10     # This is the number we are trying to guess
counter = 1     # This counts the number of tries

while counter <= 5:
    userGuess = raw_input('Guess my number: ')
    userGuess = int(userGuess)
    if userGuess == target:
        print 'You have guessed the right number! It was ' + str(target)
        break
    else:
        counter += 1
        continue
        
if counter == 5:
    print 'You did not guess the right number, it was ' + str(target)
else:
    print 'Good job!'
'''
# Version 2 - Random Target
import random

maxRange = raw_input("Guess a number between 1 and...? ")
maxRange = int(maxRange)

target = random.randrange(1,maxRange)        # Generates a random number from 1 to 100
counter = 0                             # Starts the counter for number of tries

tries = raw_input('How many tries would you like? ')
tries = int(tries)

while counter < tries:
    userGuess = raw_input('Please guess my number: ')
    userGuess = int(userGuess)
    if userGuess == target:
        print 'You have guessed the right number! It was ' + str(target) + '.'
        break
    else:
        counter += 1


if counter == tries:
    print "Unfortunately you didn't guess the right number after " + str(counter) + ' tries. The right number was ' + str(target)
else:
    print "Good Job!"


print "The game has ended."
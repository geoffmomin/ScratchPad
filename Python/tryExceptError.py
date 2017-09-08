"""
Sometimes we need the user to submit data. There might be errors. To fix, we can use the try/fix method:

    try:
        <statement that may cause an error>
    except:
        <statement to run if error occurs>
    else:
        <statement to execute if no error occurs>

So, taking the guessTheNumber.py as an example:

"""

import random

maxRange = raw_input("Guess a number between 1 and...? ")
maxRange = int(maxRange)

target = random.randrange(1, maxRange)        # Generates a random number from 1 to 100
counter = 0                             # Starts the counter for number of tries

tries = raw_input('How many tries would you like? ')
try:
    tries = int(tries)
except:
    print "Please enter an integer!"


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

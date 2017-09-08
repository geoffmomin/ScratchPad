# Using the random package in python.

'''
Packages are imported into programs by using the following:

    import <packageName>

For example:

    import random

When creating a random number, use:

    random.randrange(<lowValue>,<upToButNotIncludingHighValue>)
'''

import random

limit = raw_input("How many games shall we play? ")
limit = int(limit)
counter = 1
rock = 0
paper = 0
scissors = 0

while counter <= limit:
    choiceNumber = random.randrange(0,3)    # Gives random numbers between 0, 1 or 2
    if choiceNumber == 0:
        randomChoice = 'rock'
        rock += 1
    elif choiceNumber == 1:
        randomChoice = 'paper'
        paper += 1
    else:
        randomChoice = 'scissors'
        scissors += 1
    counter += 1

print str(rock) + ' outcomes were rock.'
print str(paper) + ' outcomes were paper.'
print str(scissors) + ' outcomes were scissors.'


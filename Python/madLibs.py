# This application is a Mad Libs game using Lists

libs = ['name', 'age', 'address', 'colour', 'size']

libs[0] = input("Please provide a funny name: ")
libs[1] = input("Please give me an age: ")
libs[2] = input("What's your favourite place? ")
libs[3] = input("And your favourite colour? ")
libs[4] = input("How would you describe your build? ")

print('There once was a ' + libs[4] + ' man named ' + libs[0] + ' who lived in ' + libs[2] + '. He was around ' +
       libs[1] + ' years old and loved the colour ' + libs[3] + '.')

# Now MadLibs with random name generator

import random     # Normally put import random at top of the code file.
names = ['Billy', 'Bobby', 'Joseph', 'Octopus', 'Lewis']
numGames = input('How many times would you like to play? ')
numGames = int(numGames)

i = 1

while i <= numGames:
    nameSelection = random.randrange(0,5)
    print('There once was a ' + libs[4] + ' man named ' + names[nameSelection] + ' who lived in ' + libs[2] +
      '. He was around ' + libs[1] + ' years old and loved the colour ' + libs[3] + '.')
    i += 1




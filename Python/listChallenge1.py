# This is a list Challenge. Similar to the modification to use a list of names, let’s modify the program to include
# a list of verbs, a list of adjectives, and a list of nouns. The program should randomly choose a name,
# a verb, an adjective, and a noun. You can put as many elements as you want into each list, and the
# program should create and print a fully randomized Mad Lib.

import random

listNouns = ['Bill', 'Bob', 'James', 'Clarke']
listVerbs = ['runs', 'jumps', 'jogs', 'dances']
listAdjectives = ['Fat', 'Skinny', 'Young', 'Old']

counter = input('How many sentences would you like to generator? ')
counter = int(counter)
i = 0

while i <= counter:

    N = random.randrange(0, len(listNouns))
    V = random.randrange(0, len(listVerbs))
    A = random.randrange(0, len(listAdjectives))

    print(listAdjectives[N] + ' ' + listNouns[V] + ' ' + listVerbs[A])

    i += 1


'''
When using loops, you may want to make a counter. Instead of using:

    counter = counter + 1

all the time, you can simply use:

    counter += 1

Similarly, for:

    counter = counter - 1

We can use:

    counter -= 1

'''

# How do we make loopAddto4.py repeat itself?

def addToTarget(target):
    total = 0
    nextToAdd = 1
    while nextToAdd <= target:
        total = total + nextToAdd
        nextToAdd += 1
    return total

run = raw_input("Do you want to run the program? ")

while run == "y" or run == 'yes' or run == 'Yes':
    userTarget = raw_input('Add all the numbers between 0 and: ')
    userTarget = int(userTarget)

    print 'The sum of all numbers from 1 to ' + str(userTarget) + ' is ' + str(addToTarget(userTarget))
    run = raw_input("Shall we run the program again? ")

print 'The program has ended.'

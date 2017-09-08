# Using loops, add up numbers from 1 to a target number

target = raw_input("Please specify your target number: ")
target = int(target)

total = 0
nextToAdd = 1

if target < 0:
    target = raw_input("Please enter a value greater than or equal to zero: ")
    target = int(target)

while nextToAdd <= target:
    total = total + nextToAdd
    print str(nextToAdd) + ' was added to ' + str(total - nextToAdd) + ' to give ' + str(total)
    nextToAdd = nextToAdd + 1

print 'The sum of all the numbers from 1 to ' + str(target) + ' is: ' + str(total)


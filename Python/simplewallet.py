# Simple program to add the value of $1 and $5 bills in a wallet

'''

Multiple line comments can be placed between triple quotations.

'''

nFives = 2
nOnes = 3
total = (nFives * 5) + nOnes
print "The total is $" + str(total)


# Simple program to calculate how much you should be paid at work

rate = 10.00
totalHours = 45
regularHours = 40
overTime = totalHours - regularHours
salary = (regularHours * rate) + (overTime * rate * 1.5)
print "You will be paid $" + str(salary)


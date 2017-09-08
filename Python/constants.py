# Constants let you assign variables that do not change

COST_PER_HAMBURGER = 3.00       # Constants are assigned with all caps
COST_PER_HOT_DOG = 2.00
COST_PER_MILK_SHAKE = 3.00

# Scope is the amount of code over which a variable is active
'''
Global variables are created at the top level of a program in the main code.
'''
# Example

TAX_RATE = 0.09
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00

def calculateCost(nSmallWidgets,nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost

total1 = calculateCost(4,8)
print ("Total for the first order is", total1)
total2 = calculateCost(12,15)
print ("Total for the second order is", total2)

# Local Variables
def myFunction():
    someVariable = 5    # Local Variable

someVariable = 10       # Global Variable replaces Local variable in myFunction
myFunction()
print (someVariable)
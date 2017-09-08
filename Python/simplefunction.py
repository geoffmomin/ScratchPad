'''
Define a function using the def

we use:
    def <functionName>(<optionalParameters>):       # Defines a functions parameters
        <indented statements>                       # The function body
'''

def times5(x):
    x = x * 5
    print x
    return

times5(5)

def getGroceries():
    print "milk"
    print "flour"
    print "sugar"
    print "squash"
    print #blank line

getGroceries() #calls the function getGroceries. Must have () even if not parameters.
getGroceries()

#Show how a function can call another function

def separateRuns():
    print "********************"
    print #blank Line

def getGroceriesNew():
    print "milk"
    print "flour"
    print "sugar"
    print "squash"
    print #blank line
    separateRuns() #calls the function separateRuns.

getGroceriesNew()
getGroceriesNew()

mustget = "juice"
def groceryList(item1,item2,item3):
    print item1
    print item2
    print item3
    print "eggs"
    print "water"
    print "apples"
    print #Blank Line

groceryList(mustget,"limes","eggplant")
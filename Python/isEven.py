# This program determines if an integer is odd or even

def isEven(x):
    if int(x) % 2 == 0:
        return True
    else:
        return False

number = raw_input("Please enter your number: ")

if isEven(number) == True:
    print str(number) + " is true!"
else:
    print str(number) + " is false!"

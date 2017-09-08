#  This is a programming challenge

def negativePositiveZero(x):
    if int(x) < 0:
        return "negative"
    elif int(x) == 0:
        return "zero"
    else:
        return "positive"

number = raw_input("Please enter a number: ")
print str(number) + " is " + str(negativePositiveZero(number))
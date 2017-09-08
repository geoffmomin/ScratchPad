#   This snippet uses IF/ELIF/ELSE constructs to determine absolute values

number = raw_input("Please enter a number: ")

def absoluteValue(number):
    if number >= 0:
        output = number
    else:
        output = number * -1
    return output

final = absoluteValue(int(number))

print "The absolute value of " + number + " is " + str(final)
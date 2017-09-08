# This is a program to determine if the two sides represent a square.

def isSquare(length,width):
    if length == width:
        return "true"
    else:
        return "false"


user_length = raw_input("Please enter the length measurement: ")
user_width = raw_input("Please enter the width measurement: ")

if isSquare(user_length,user_width) == "true":
    print "You describe a square"
else:
    print "You describe a rectangle"
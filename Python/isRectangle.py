# This function determines if the sides form a rectangle

def isRectangle (t,l,r,b):
    if int(t) == int(b) and int(l) == int(r):
            return True
    else:
        return False

top = raw_input("Length of the top side: ")
bottom = raw_input("Length of the bottom side: ")
left = raw_input("Length of the left side: ")
right = raw_input("Length of the right side: ")

if isRectangle(top,left,right,bottom) == True:
    print "You have a rectangle!"
else:
    print "You don't have a rectangle"

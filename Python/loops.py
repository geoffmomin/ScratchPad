# A loop is a block of code that repeats until a certain condition is met

'''
In python, a loop is entered with a while statement. The generic form of a while statement is:

    while <Boolean expression>: #as long as the expression to True
        <indented block of code>

'''

looping = True
while looping == True:
    answer = raw_input("Please type the letter 'a': ")
    if answer == "a":
        looping = False # we're done
    else:
        print "Come on, type an 'a'! "

print "Thanks for typing an 'a'"


import random #Allows us to use random numbers
while True: #Creates a loop while True (there is no false scenario)
    print #Prints a blank line

    usersQuestion = raw_input("Ask the Magic 8 Ball a question (Return or Enter to quit): ") #raw_input begs a question
    if usersQuestion == "":
        break #Closes the program

    randomAnswer = random.randrange(8) #Pick a random number between 0 and 7

    if randomAnswer == 0:
        print "It is certain."

    elif randomAnswer == 1:
        print "Absolutely!"

    elif randomAnswer == 2:
        print "You may rely on it."

    elif randomAnswer == 3:
        print "Answer is foggy, ask again later."

    elif randomAnswer == 4:
        print "Concentrate and ask again."

    elif randomAnswer == 5:
        print "Unsure at this point, try again."

    elif randomAnswer == 6:
        print "No way, dude!"

    elif randomAnswer == 7:
        print "No, no, no, no, no."
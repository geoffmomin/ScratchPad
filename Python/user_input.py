'''

We use raw_input to request input from the user and save the input to a variable. 

'''

faveColour = raw_input("What is your favourite colour? ")
print "Your favourite colour is", faveColour


faveNumber = raw_input("What is your favourite number? ")
print "Your favourite number is", faveNumber

print int(faveNumber) + 1

price = raw_input("What is the price? ")
print "You have paid $" + price
total = float(price) * 1.13
print "With tax, the total comes to $" + str(total)

# To convert between strings, floats, integers

number = raw_input("Please input a number ")     # This returns a string
number = int(number) * 2                        # Converts number to integer before multiplying
print "Your new number is", str(number)         # Converts back to string to print

price = raw_input("Please input a price ")
total = float(price) * 1.13                     # Converts price to float before multiplying
print "Your total with tax is $" + str(total)   # Converts total to string to print
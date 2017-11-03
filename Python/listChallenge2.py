# In this list challenge, we're writing a program that starts with
# a list of numbers to add all the numbers in the list

numbersList = [23, -10, 37, 4.5, 0, 123.4]
total = 0

for items in numbersList:
    total = total + items

print(str(total))


# Another way

i = 0
total = 0

while i <= len(numbersList)-1:
    total = total + numbersList[i]
    i += 1

print(str(total))

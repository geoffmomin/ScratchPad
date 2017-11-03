# This program calculates all the integers from 1 up to and including the
# user-prompted integer

userNumber = input("Please pick any number: ")
numbers = range(1, int(userNumber)+1)
total = 0

for items in numbers:
    total = total + items

print('The sum of all numbers from 1 to ' + userNumber + ' is ' + str(total))



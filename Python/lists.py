"""
A list is a group of data with a single given name. A list is a new data type, like integer, string, float and boolean.
Example of lists:
    cereal
    milk
    orange juice
    hot dogs
    gum
And:
    99
    72
    88
    82
    54

In python, we use [] to denote lists:

    variable = [<element>,<element>,...<element>]

In python, lists begin with 0.

"""

shoppingList = ['cereal', 'milk', 'orange juice', 'hot dogs', 'gum']
scoresList = [99, 72, 88, 82, 54]
mixedList = [True, 5, 'some string', 123.45]
emptyList = []

#   print mixedList
#   print type(mixedList)
#   print emptyList

# To access a variable in a list use: variableName[index]. Negative indices will count backwards from -1.

#   secondItem = shoppingList[1]
#   print secondItem

#   lengthShoppingList = len(shoppingList)
#   print lengthShoppingList
#   myIndex = raw_input("Please enter an index between 0 and " + str(lengthShoppingList) + ": ")
#   print shoppingList[int(myIndex)]

# To change a value in a list, use: listName[index] = newItem

print(shoppingList)
shoppingList[3] = 'apples'
print(shoppingList)

# You can use negative indices to count backwards. i.e. -1 means last.

print(shoppingList[-1])

# To determine the number of elements in a list

print("There are " + str(len(shoppingList)) + " elements in the list: shoppingList")
print(shoppingList)

# Indexing

greeting = "Hello"
print(greeting[0])
print(greeting[-1])

# Slicing

url = '<a href="http://google.com">Google</a>'
print(url[9:26])
print(url[9:-12])

# Multiplication

print([42] * 10)

# Membership

print('o' in greeting)
print('f' in greeting)

# Length, Minimum and Maximum

numbers = [100, 54, 67]

print(len(numbers))
print(min(numbers))
print(max(numbers))

# Deleting from List

names = ['Geoff', 'James', 'John']
print(names)
del names[2]
print(names)


# Convert string to list

hello = list('Hello')
print(hello)

# Variables should not begin with numbers.

age = 0                 # integer number
gpa = 3.4               # float number
male = True             # boolean
name = "Geoffrey"       # string
location = "Canada"     # Read as "the location is set to Canada"

age = 23                # It's easy to change the values of a variable
yourAge = age + 2

print("Hi my name is " + name + " and I am " + str(age) + " years old. I go to school in " + location + " and my GPA is " + str(gpa))
print("Hi my name is ", name, "and I am ", str(age), "years old.")
print("Your age is " + str(yourAge))
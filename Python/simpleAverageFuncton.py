def calculateAverage(param1,param2,param3,param4):
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average,total        #Return multiple variables


average1,total1 = calculateAverage(135,175,235,275)

print "The average is",average1,"and total is",total1

num1 = 15
num2 = 20
num3 = 25
num4 = 30

average2,total2 = calculateAverage(num1,num2,num3,num4)
print "The average is",average2,"and total is",total2
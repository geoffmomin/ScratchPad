''' 
To convert C to F, multiply by 1.8 and add 32. F = (1.8 * C) + 32
To convert F to C, subtract 32, and multiply by 0.5556. C = (F-32) * 0.5556
'''

def F2C(farenheit):
    C = (farenheit-32) * 0.5556
    return C

def C2F(celsius):
    F = (celsius * 1.8) + 32
    return F

conv2C = F2C(32)
conv2F = C2F(100)

print "32F is " + str(conv2C) + "C while 100C is " + str(conv2F) + "F"
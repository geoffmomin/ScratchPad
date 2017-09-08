# To break a loop, use break. To continue a loop use continue.

while True:
    line = raw_input("Should we continue? ")
    if line == "yes":
        continue
    else:
        break

print 'finished.'


# This is a random number generator for the counts detected from Po 210

import random
import csv

i = 1
data = []

while i <= 15:
    if i % 3 == 2:
        N = random.randrange(2, 7)
        data.append(N)
    elif i % 3 == 1:
        N = random.randrange(1, 5)
        data.append(N)
    else:
        N = 3
        data.append(N)
    i += 1

print(data)
# out = csv.writer(open('Po210Random.csv', 'w'), delimiter=',', quoting=csv.QUOTE_ALL)
# out.writerow(data)

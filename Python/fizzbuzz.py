# FizzBuzz Test. Print all numbers 1-100 where multiples of 3 = Fizz, 5 = Buzz, and 3 and 5 = FizzBuzz

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    else:
        print(str(i))

    i += 1


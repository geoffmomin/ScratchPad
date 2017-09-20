# This program spits out a date from input values

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
suffixes = ['st', 'nd', 'rd', 'th']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day: ')

day = int(day)
month = int(month)

if day >= 4:
    day = 4


print('The date is ' + months[month-1] + ' ' + str(day) + suffixes[day-1] + ', ' + year)



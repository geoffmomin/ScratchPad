# This program uses IF statements to calculate shipping

def shipping(country, widgets):
    if (country == "USA") or (country == "US") or (country == "America"):
        if widgets <= 50:
            return 6.25
        elif widgets > 50 and widgets <= 100:
            return 9.50
        elif widgets > 100 and widgets <= 150:
            return 12.75
        else:
            return 15.00
    elif (country == "Canada"):
        if widgets <= 50:
            return 8.25
        elif widgets > 50 and widgets <= 100:
            return 12.50
        elif widgets > 100 and widgets <= 150:
            return 18.00
        else:
            return 25.00
    else:
        return 0

userWidgets = raw_input("How many widgets would you like to buy? ")
userWidgets = int(userWidgets)

userCountry = raw_input("Where would you like us to ship your widgets? ")

if shipping(userCountry,userWidgets) > 0:
    print "Your shipping costs are $" + str(shipping(userCountry,userWidgets)) + " to ship " + str(userWidgets) + " widgets to " + userCountry
else:
    print "Unfortunately we do not ship to your country."


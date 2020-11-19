# Determine cheapest shipping method and shipping cost based on package weight

# Get ground shipping cost
def ground_shipping(lbs):
    if lbs <= 2:
        return lbs * 1.5 + 20
    elif lbs <= 6:
        return lbs * 3 + 20
    elif lbs <= 10:
        return lbs * 4 + 20
    else:
        return lbs * 4.75 + 20

# Get drone shipping cost
def drone_shipping(lbs):
    if lbs <= 2:
        return lbs * 4.50
    elif lbs <= 6:
        return lbs * 9
    elif lbs <= 10:
        return lbs * 12
    else:
        return lbs * 14.25

# Set static premium ground shipping cost
premium_shipping = 125

# Calculate cheapest method and return total cost
def shipping_calc():
    weight = float(input('Enter the package weight in lbs.: ')) # Get the package weight

    if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping: # Ground shipping is the cheapest
        print('The cheapest shipping method is GROUND SHIPPING')
        print('It will cost $' + str(ground_shipping(weight)))
    elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping: # Drone shipping is the cheapest
        print('The cheapest shipping method is DRONE SHIPPING')
        print('It will cost $' + str(drone_shipping(weight)))
    else:
        print('The cheapest shipping method is PREMIUM GROUND SHIPPING') # All others - basically just when premium ground is the cheapest
        print('It will cost $' + str(premium_shipping))


shipping_calc()


def convert(cups):
    ml = round((float(cups) * 240), 1)
    return ml


print("This program will convert cups to milliliters")
cups = raw_input("How many cups? ")

milli = convert(cups)
print (cups + " cups is equal to " + str(milli) + " milliliters")
a = 7
b = 11

def over_the_road(address, n):
    print((address + ((n - (round(address / 2))) * 2) + 1) - (2 * round(address / 2)) + 2)

over_the_road(a, b)

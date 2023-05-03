def narcissistic(value):
    return sum([int(n) ** len(str(value)) for n in str(value)]) == value

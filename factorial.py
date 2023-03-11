def factorial(n):
    counter = n - 1
    number = n
    if n == 0:
        return 1
    else:
        while counter > 0:
            number = counter * number
            counter -= 1
        return number

def printer_error(s):
    return (str(len(list(char for char in s if char > "m"))) +
            "/" + str(len(s)))

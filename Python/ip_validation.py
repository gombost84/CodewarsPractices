def is_valid_IP(strng):
    list_items = [elem for elem in strng.split('.')]

    if len(list_items) != 4:
        return False

    for item in list_items:

        try:
            int(item)
        except ValueError:
            return False

        if len(item) == 0:
            return False

        if item[0] == '0' and len(item) > 1:
            return False

        if any(symbol in [' ', '\n'] for symbol in item):
            return False

        if int(item) not in range(0, 256):
            return False

    return True

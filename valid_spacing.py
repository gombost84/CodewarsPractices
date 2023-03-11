def valid_spacing(s):
    print(s)
    if len(s) == 0:
        return True
    elif len(s) == 1 and s != ' ':
        return True
    elif s[0] == ' ':
        return False
    elif s[-1] == ' ':
        return False
    else:
        for x in range(0, len(s) - 1):
            if s[x] + s[x + 1] == '  ':
                return False
        return True
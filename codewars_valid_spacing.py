def valid_spacing(s):
    if len(s) == 0:
        return True
    elif len(s) == 1 and s != ' ':
        return True
    elif s[0] != ' ' and s[-1] != ' ':
        x = 0        
        while x < len(s):
            print(s[x] + s[x + 1])
            if s[x] + s[x + 1] == '  ':
                return False
                x += 1
                break
            else:
                pass
            return True
    else:
        return False

valid_spacing('cod  ewars')

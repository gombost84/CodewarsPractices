def last_survivor(letters, coords):
    s = list(letters)
    while len(coords) > 0:
        del (s[coords[0]])        
        coords.remove(coords[0])
    return "".join(s)

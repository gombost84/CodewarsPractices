def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    left_points = 0
    right_points = 0

    for char in fight:
        if char in left.keys():
            left_points += left.get(char)
            continue
        elif char in right.keys():
            right_points += right.get(char)
            continue
        else:
            continue

    if left_points == right_points:
        return '''Let's fight again!'''
    elif left_points > right_points:
        return 'Left side wins!'
    else:
        return 'Right side wins!'

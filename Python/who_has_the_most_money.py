def most_money(students):
    most = {}
    for s in students:
        most[s.name] = s.fives * 5 + s.tens * 10 + s.twenties * 20
    if len(most) == 1:
        return list(most)[0]
    elif all(x == max(most.values()) for x in most.values()):
        return 'all'
    for name, money in most.items():
        if money == max(most.values()):
            return name

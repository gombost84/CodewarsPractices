def part(arr):
    related_terms = ['Partridge', 'PearTree', 'Chat', 'Dan',
                     'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    exclamation_counter = 0
    for item in arr:
        if item in related_terms:
            exclamation_counter += 1
    if exclamation_counter > 0:
        return "Mine's a Pint" + "!" * exclamation_counter
    else:
        return "Lynn, I've pierced my foot on a spike!!"

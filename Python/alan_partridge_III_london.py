def alan(arr):
    stations = {'Rejection': 0, 'Disappointment': 0,
                'Backstabbing Central': 0, 'Shattered Dreams Parkway': 0}
    for station in arr:
        if station in stations.keys():
            stations[station] += 1
    if all(value != 0 for value in stations.values()):
        return "Smell my cheese you mother!"
    else:
        return "No, seriously, run. You will miss it."

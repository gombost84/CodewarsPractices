def small_enough(array, limit):
    T = list(map(lambda x: True if x <= limit else False, array))
    if all(T):
        return True
    else:
        return False
    
print(small_enough((66, 101), 200))

def keep_order(ary, val):
    if len(ary) == 0 or val <= ary[0]:
        return 0
    elif val > ary[-1]:
        return len(ary)
    for x in range(len(ary)):
        if (ary[x] < val and ary[x + 1] >= val):
            return x + 1

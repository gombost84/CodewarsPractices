dad_years_old = 22
son_years_old = 1
dad = dad_years_old
son = son_years_old

while son > 0:
    if dad == 2 * son:
        print(-1 * (dad - dad_years_old))
        break
    dad -= 1
    son -= 1

while dad + 1 != 2 * son:
    if dad == 2 * son:
        print(dad - dad_years_old)
        break
    dad += 1
    son += 1

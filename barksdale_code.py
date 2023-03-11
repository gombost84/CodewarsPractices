def decode(string):
    dict = {0 : 5, 1 : 9, 2 : 8, 3 : 7, 4 : 6, 5 : 0, 6 : 4, 7 : 3, 8 : 2, 9 : 1}
    list = [char for char in string]
    for item, value in enumerate(list):
        for x in dict.keys():
            if int(value) == x:
                list[item] = str(dict[x])
    print("".join(list))

decode("4103432323")

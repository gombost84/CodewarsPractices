a1 = "aretheyhere"
a2 = "yestheyarehere"

def longest(a1, a2):
    print(''.join(sorted(list(dict.fromkeys(char for char in (a1 + a2))))))

longest(a1, a2)

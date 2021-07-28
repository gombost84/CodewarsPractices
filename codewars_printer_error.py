def printer_error(s):
    return(str(len(list(char for char in s if char > "n"))) + "/" + str(len(s)))

print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))

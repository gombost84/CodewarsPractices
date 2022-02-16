def is_valid_IP(strng):
    list_items = [int(elem) for elem in strng.split('.')]
    
def validation(listing):
    if len(listing) != 4:
        print('False')
    elif list(int(item))[0] == 0:
        print('False')
    for item in listing:        
        if int(item) not in range(0, 256):
            print('False')
        else:
            print('True')     


is_valid_IP('123.456.789.0')


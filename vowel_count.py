def get_count(input_str):
    num_vowels = [elem for elem in input_str if elem in ['a', 'e', 'i', 'o', 'u']]

    return len(num_vowels)

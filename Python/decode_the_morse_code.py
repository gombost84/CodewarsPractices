from preloaded import MORSE_CODE


def decode_morse(morse_code):

    words = [MORSE_CODE[x] if x not in ['   ', ' ', ''] else ' ' for x in morse_code.split(' ')]
    sentence = ''.join(words).replace('  ', ' ')
    return sentence.lstrip().rstrip()

def spin_words(sentence):
    split_words = sentence.split(' ')
    new_sentence = []
    for word in split_words:
        if len(word) < 5:
            new_sentence.append(word)
        elif len(word) > 4:            
            new_sentence.append(word[::-1])
    return ' '.join(new_sentence)

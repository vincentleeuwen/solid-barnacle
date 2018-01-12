def abbreviate(words):
    abbr = []
    for word in words.replace('-', ' ').split(' '):
        abbr.append(word[0].upper())
    return ''.join(abbr)
